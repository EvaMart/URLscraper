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
url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"

def parseInput(InputPath):
    '''
    This function takes the input file and builds a list of urls
    required: the input path. Line format in input file: <url>\t<name>\n
    returns: a lis of urls in the file
    '''
    urls_file = open(InputPath, 'r')
    urls = {}
    URLs = []
    counter = 1
    counter_valid = 0
    for line in urls_file:
        if len(line.split('\t')) != 2:
            print("Input file line %s skipped: impossible to parse, number of columns != 2."%(counter))
        else:
            url = line.split('\t')[0]
            name = line.split('\t')[1].split('\n')[0]
            if "galaxy" not in url:
                urls[check_protocol(url)] = name
                URLs.append(check_protocol(url))
                counter_valid += 1
        counter += 1
    print("Number of URLs to be analyzed: %s"%(counter_valid))
    if urls == []:
        print("No URLs to analyze")
        return(None)
    else:
        return(URLs, urls)


def check_protocol(url):
    '''
    '''
    if re.match('^http', url) != None: # To be changed for proper regex (beginning of line)
        return(url)

    else:
        return('https://' + url)



def getHTML(url, verb=False):
    from bs4.dammit import EncodingDetector

    try:
        re = session.get(url, headers=headers, timeout=(10, 30))

    except:
        return(None)

    else:
        # dealing with encoding
        http_encoding = re.encoding if 'charset' in re.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(re.content, is_html=True)
        encoding = html_encoding or http_encoding

        if 'text/html' in re.headers.get('content-type'):
        # generating BeautifulSoup object
            bsObj = BeautifulSoup(re.content, 'html5lib', from_encoding=encoding)
            return(bsObj)
        else:
            return(None)

    #print(re.status_code)





class InternalTextsScraper(object):

    def __init__(self, URLs, depth, LinksOut, TimeOut):
        self.URLs = URLs
        self.depth = depth
        self.URLsDict = {}
        self.Texts = {}
        self.LinksOut =  LinksOut
        self.TimeOut = TimeOut
        self.oplinks = 'repos'

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
        for url in self.URLs:
            try:
                re = session.get(url, headers=headers, timeout=(10, 30))
                domain = re.url.split('/')
                if len(domain) > 3:
                    domain = '/'.join(domain[:-1])
                else:
                    domain = '/'.join(domain)
                #print('Analysing URL %s: %s'%(count, domain))
                links = set()
                links.add(url)
                links = self.crawlWithDepth(urls = links, domain = domain)
                scrapped_links[url] = links
                print(links)
                count += 1
            except:
                continue

        self.URLsDict = scrapped_links



    def crawlWithDepth(self, urls, domain):
        '''
        This function returns a set of URLs 'urls' that result from their crawling with depth 'depth'.
        '''
        count = 0
        URLs = set(urls)

        while count < self.depth:
            urls = self.single_crawl(urls, domain)
            for e in urls:
                URLs.add(e)
            count += 1

        return(URLs)



    def single_crawl(self, urls, domain):
        '''
        This function returns a set containing the links (urls) in a list of htmls (BeautifulSoup object)
        '''
        total_urls = urls

        for link in urls:
            #print(link)
            bsObj = getHTML(link)

            total_urls= total_urls.union(self.getAllLinks(link, bsObj, domain))

        return(total_urls)


    def getAllLinks(self, URL, bsObj, domain):
        links = set()

        if bsObj == None:
            #print("bsObj is None")
            return()

        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:

                if self.isValidLink(link.attrs['href'])== True: # if link is really an URL

                    url = urljoin(URL, link.attrs['href']) # resolve URL
                    #print(domain)
                    #if self.oplinks == 'repos':
                    #    if 'github.com' not in URL and 'sourceforge.net' not in URL:
                    #        if 'github.com' in url or 'sourceforge.net' in url:
                                #print('+1')
                    toWrite = '%s\t%s\n'%(domain, url)
                    self.LinksOut.write(toWrite)

                    if domain in url: #if link is internal, we add it
                        #print("domain: " + domain)
                        #print("internal: " + url)
                        links.add(url)
                    else: # if the link is external, we skip it
                        #print("domain: " + domain)
                        #print("external: " + url)
                        continue
        return(links)


    def getGithubs(self):
        Githubs = {}
        for url in self.URLsDict.keys():
            foundGithubs = []
            if getHTML(url) != None :
                bObj = getHTML(url)
                links = [li.attrs ["href"] for li in bObj.findAll("a") if 'href' in li.attrs]
                for link in links:
                    if self.isValidLink(link)== True and 'github' in link and link != url:
                        foundGithubs.append(link)
            Githubs[url] = foundGithubs
        print(Githubs)
        return(Githubs)


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



    def html2text(self, url, filename):
        #print('URL: ' + url)
        try:
            re = session.get(url, headers=headers, timeout=(10, 30))
        except: # this handles all any connection error occurring
            print('Cannot connect to ' + url)
            return(None)
        else:
            print(re.headers)
            if 'Content-Type' in re.headers.keys() and 'text/html' in re.headers.get('Content-Type'):
                h = html2text.HTML2Text()
                h.ignore_images = True
                h.ignore_links = True
                t = re.text
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
            req = getHTML(url)
            if req != None:

                for link in req.findAll("a"):
                    if "href" in link.attrs:
                        if doire.match(link.attrs["href"]) != None:
                            print(link.attrs["href"])
                        elif 'journal' in link.attrs["href"]:
                            print(link.attrs["href"])