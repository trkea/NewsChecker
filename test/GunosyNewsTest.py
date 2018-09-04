import unittest
import sys
sys.path.append('../../NewsChecker')
from src import GunosyNews
sys.path.append('/src')

class GunosyNewsTest(unittest.TestCase):

	def test_get_html(self):
	    news = GunosyNews.GunosyNews('http://okuya-kazan.hatenablog.com/entry/2017/06/24/013541')
	    html_str = news.get_html().text
	    self.assertTrue(html_str.find('<!DOCTYPE html>'))

if __name__ == '__main__':
	unittest.main()