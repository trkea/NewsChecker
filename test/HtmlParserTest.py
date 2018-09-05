import urllib.request
import sys
sys.path.append("../../NewsChecker")
import unittest
from src import HtmlParser as hp

class htmlParserTest(unittest.TestCase):

	def test_get_html(self):

	    html_str = hp.HtmlParser.get_html('',url="https://www.google.co.jp/").text
	    self.assertTrue(html_str.find("<!DOCTYPE html>"))

if __name__ == '__main__':
    unittest.main()	    