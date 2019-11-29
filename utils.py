import argparse
import requests
import re
from bs4 import BeautifulSoup
import html2text ## http://www.aaronsw.com/2002/html2text/
import json
from urllib.parse import urljoin
import time
import os

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

def parseInput(InputPath):
    '''
    This function takes the input file and builds a list of URLs
    required: the input path. Line format in input file: <url>\t<name>\n
    returns: a lis of urls in the file
    '''
    urls_file = open(InputPath, 'r')
    urls = {}
    URLs = set()
    counter = 1
    for line in urls_file:
        if len(line.split('\t')) != 2:
            print("Input file line %s skipped: impossible to parse, number of columns != 2."%(counter))
        else:
            url = line.split('\t')[0]
            name = line.split('\t')[1].split('\n')[0]
            if url not in URLs:
                urls[check_protocol(url)] = name
                URLs.add(check_protocol(url))
        counter += 1
    print("Number of URLs to be analyzed: %s"%(len(URLs)))
    if urls == []:
        print("No URLs to analyze")
        return(None)
    else:
        URLs = set(URLs)
        return(URLs, urls)


def check_protocol(url):
    '''
    '''
    if re.match('^http', url) != None: # To be changed for proper regex (beginning of line)
        return(url)

    else:
        return('https://' + url)



def getHTML(url, verb=False):
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    from bs4.dammit import EncodingDetector
    import urllib

    try:
        req = session.get(url, headers=headers, timeout=(20, 50), verify=False)
        #req = urllib.request.urlopen(url)

    except Exception as e:
        print(e)
        return(None)

    else:
        if 'text/html' in req.headers.get('content-type'):
            return(req)
        else:
            return(None)

    #print(re.status_code)





class InternalTextsScraper(object):

    def __init__(self, URLs, urls, depth, LinksOut, TimeOut, outname):
        self.URLs = URLs
        self.urls = urls
        self.depth = depth
        self.URLsDict = {}
        self.Texts = {}
        self.LinksOut =  LinksOut
        self.TimeOut = TimeOut
        self.oplinks = 'repos'
        self.outname = outname

        self.counter = 0

    # The links scraper
    def extractLinks(self):
        '''
        This function gets the internal links (depth = depth) for all the URL
        in the list URLs.
        The goal is creating a dict sefl.URLsDict of the form: url:[internal links]
        Used by self.ScrapText()
        '''
        self.LinksOut.write('url\thref\turl\n')
        scrapped_links = {}
        count = 1
        import difflib
        for url in self.URLs:
            try:
                req = getHTML(url)

                domain = req.url.split('/')

                if len(domain) > 3:
                    domain = '/'.join(domain[:-1])
                else:
                    domain = '/'.join(domain)
                print('Analysing URL %s: %s'%(count, domain))
                links = set()
                links.add(url)
                self.counter = 1
                self.extractSingleText(url, url)
                links = self.crawlWithDepth(urls = links, domain = domain, url =url)
                scrapped_links[url] = links
                #print(links)
                count += 1
            except Exception as e:
                print('Failing: ' + '\t' + url)
                print(e)
            
                continue

        self.URLsDict = scrapped_links



    def crawlWithDepth(self, urls, domain, url):
        '''
        This function returns a set of URLs 'urls' that result from their crawling with depth 'depth'.
        '''
        count = 0
        URLs = set(urls)

        while count < self.depth:
            urls = self.single_crawl(urls, domain, url)
            for e in urls:
                URLs.add(e)
            count += 1

        return(URLs)



    def single_crawl(self, urls, domain, url):
        '''
        This function returns a set containing the links (urls) in a list of htmls (BeautifulSoup object)
        '''
        total_urls = urls

        for link in urls:
            # dealing with encoding
        
            bsObj = BeautifulSoup(getHTML(link).content, 'html5lib')
            
            total_urls= total_urls.union(self.getAllLinks(link, bsObj, domain, url))

        return(total_urls)


    def getAllLinks(self, URL, bsObj, domain, url):

        links = set()

        if bsObj == None:
            #print("bsObj is None")
            return()

        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:

                if self.isValidLink(link.attrs['href'])== True: # if link is really an URL

                    cur_url = urljoin(URL, link.attrs['href']) # resolve URL

                    if domain in cur_url: #if link is internal, we add it

                        if cur_url not in links:

                            links.add(cur_url)
                            self.counter += 1
                            self.extractSingleText(url, cur_url)

                    else: # if the link is external, we skip it
                        #print("domain: " + domain)
                        #print("external: " + url)
                        continue
        return(links)


    def isValidLink(self, url):
        '''
        This function takes an url as an argument and returns True if it is valid and false if it is not.
        A link is considered valid if it is a link to a url, either absolute or not.
        '''
        p = re.compile("#")
        p2 = re.compile("\$")
        pjava = re.compile("javascript:")

        if p.match(url) != None or p2.match(url)!= None or pjava.match(url)!= None:
            return(False)
        elif url in ['', ' ']:
            return(False)
        #elif "galaxy" in url or "github" in url:
        #    return(False)
        else:
            return(True)


    # The text extractor
    def extractText(self, outname, urls):
        '''
        This function extracts the text in self.URLsDict
        Used by self.ScrapText()
        It writes the md of each url in a file
        '''
        for url in self.URLsDict.keys(): # for each parent
            inter_texts = {}
            counter  = 0
            for inter_link in self.URLsDict[url]: # for each internal url
                #print('getting text of ' + inter_link)
                start = time.clock()

                filename = outname + "/" + urls[url] + "/" + urls[url] + "_url_" + str(counter) + ".md"
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                #print(inter_link)
                text = self.html2text(inter_link, filename)
                # for each master url, this dict stores the md text of the children
                inter_texts[inter_link] = text

                end = time.clock()
                elapse = end - start

                self.TimeOut.write('%s\t%s\t%f\n'%(url, inter_link, elapse))
                counter += 1
            self.Texts[url] = inter_texts

        '''
        with open(outname + '.json', 'w') as fp:
            json.dump(self.Texts, fp, sort_keys=True, indent=4)
        '''

    def extractSingleText(self, url,  inter_link):
        '''
        It writes the md of each url in a file
        '''
        start = time.clock()
        filename = self.outname + "/" + self.urls[url] + "/" + self.urls[url] + "_url_" + str(self.counter) + ".md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        #print(inter_link)
        self.html2text(inter_link, filename)
        # for each master url, this dict stores the md text of the children

        end = time.clock()
        elapse = end - start

        self.TimeOut.write('%s\t%s\t%f\n'%(url, inter_link, elapse))



        '''
        with open(outname + '.json', 'w') as fp:
            json.dump(self.Texts, fp, sort_keys=True, indent=4)
        '''

    def html2text(self, url, filename):
        #print('URL: ' + url)
        try:
            req = session.get(url, headers=headers, timeout=(10, 30))
        except: # this handles all any connection error occurring
            print('Cannot connect to ' + url)
            return(None)
        else:
            #print(re.headers)
            if 'Content-Type' in req.headers.keys() and 'text/html' in req.headers.get('Content-Type'):
                h = html2text.HTML2Text()
                h.ignore_images = True
                h.ignore_links = True
                t = req.text
                text = h.handle(t)
                text = text.replace("\n\n", "<m>")
                text = text.replace("\n ", "<m>")
                text = text.replace(" \n", "<m>")
                text = text.replace("\n", " ")
                pars = text.split("<m>")
                paragraphs = ''
                outParaFil = open(filename, 'w')
                outParaFil.write("<-- " + url + "-->\n")
                for par in pars:
                    if par.lstrip() not in ['', ' ']:
                        if len(par.lstrip().split(" ")) > 3:
                            paragraphs = paragraphs + "\n" + par.lstrip()

                #print(paragraphs)
                outParaFil.write(paragraphs)
                return(paragraphs)


    def extractCitations(self):
        for url in self.URLsDict.keys(): # for each parent
            print("searching cit of: " + url)
            for inter_link in self.URLsDict[url]: # for each internal url
                self.extractCit(inter_link)



    def extractCit(self, url):
        doire = re.compile('\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')
        if self.isValidLink(url) == True:

            # HTML here!!!!!

            req = BeautifulSoup(getHTML(url).content, 'html5lib')
            if req != None:

                for link in req.findAll("a"):
                    if "href" in link.attrs:
                        if doire.match(link.attrs["href"]) != None:
                            print(link.attrs["href"])
                        elif 'journal' in link.attrs["href"]:
                            print(link.attrs["href"])

    def getGithubs(self):
        Githubs = {}
        for url in self.URLsDict.keys():
            foundGithubs = []
            #### getHTML!!!!
            if getHTML(url) != None : 

                bsObj = BeautifulSoup(getHTML(url).content, 'html5lib')
                links = [li.attrs ["href"] for li in bsObj.findAll("a") if 'href' in li.attrs]

                for link in links:

                    if self.isValidLink(link)== True and 'github' in link and link != url:

                        foundGithubs.append(link)

            Githubs[url] = foundGithubs

        print(Githubs)
        return(Githubs)
