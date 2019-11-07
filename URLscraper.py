import pandas as pd
import argparse
from utils import parseInput
from utils import InternalTextsScraper


def json2table(inputf, outputf):
    jsonfile = open(inputf,'r')
    texts = json.load(jsonfile)
    outtable = open(outputf, 'w')
    for url in texts:
        try:
            texts.keys()
        except AttributeError as err:
            print(err)
            continue
        else:
            for link in texts[url]:
                if texts[url][link] != None:
                    #print(texts[url][link])
                    for par in texts[url][link]:
                        outtable.write(link + '\t' + par + '\n')



    # parse input

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This is a description of the program')
    parser.add_argument("urls", help='Path to the file where URLs to scrap are stored.')
    parser.add_argument("depth", type=int, choices= [1,2],help='Depth of the scraping.')
    parser.add_argument("outname", help='output name')
    parser.add_argument("text", help='text extracion: True or False')

    args = parser.parse_args() # access: args.depth, args.urls, arg.outname


    urls = args.urls
    URLs, urls = parseInput(urls)
    depth = args.depth
    outname = args.outname

    # If input ok, then extract text
    if URLs != None:

        # Initialize the scraper
        LinksOut = open('Links'+ outname +'.txt', 'w')
        TimeOut = open('Time' + outname + '.txt','w' )

        T = InternalTextsScraper(URLs = URLs, depth = depth, LinksOut=LinksOut, TimeOut=TimeOut)

        # Scrap the internal links for the desired depth
        T.extractLinks()
        #print(T.URLsDict)
        #githubs = T.getGithubs()

        # Extract the text if option text=True
        if args.text == 'True':
            T.extractText(outname, urls)
    # Else, inform that the scraper was not even initialized
    else:
        print('No URLs were provided, no scraping was performed')
