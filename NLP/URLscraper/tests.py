import sys
from pprint import pprint

import unittest

import  utils


class Test_isValidLink(unittest.TestCase):

    def test_isValidLink(self):
        testclass = utils.InternalTextsScraper(
            URLs=set(['http://daweb.ism.ac.jp/yoshidalab/motif']),
            urls={'http://daweb.ism.ac.jp/yoshidalab/motif': 'motif'},
            depth=2,
            LinksOut=None,
            TimeOut=None,
            outname='2urls',
            textExtraction=True)

        mock_valid_urls = (
            'https:wikipedia.es',
            '#citations'
        )

        mock_invalid_urls = (
            'www.jasvascript.com'
        )
        
        for url in mock_valid_urls:
            self.assertTrue(testclass.isValidLink(url))

        for url in mock_invalid_urls:
            self.assertFalse(testclass.isValidLink(url))



class Test_getAllLinks(unittest.TestCase):

    def test_getAllLinks_single_crawl(self):
        testclass = utils.InternalTextsScraper(
            URLs=set(['http://daweb.ism.ac.jp/yoshidalab/motif']),
            urls={'http://daweb.ism.ac.jp/yoshidalab/motif': 'motif'},
            depth=2,
            LinksOut=None,
            TimeOut=None,
            outname='2urls',
            textExtraction=True)

        from bs4 import BeautifulSoup

        mock_p = {
            'urls':[],
            'domain':'',
            'url':''
        }  
        
       
        mock_final_result = [] 

        for url in mock_valid_urls:
            self.assertEqual(testclass.single_crawl(mock_p['urls'], mock_p['domain'], mock_p['url']))
            

if __name__ == "__main__":
    unittest.main()