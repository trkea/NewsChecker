import unittest
import sys
sys.path.append("../../NewsChecker")
from src import GunosyNews as gn
from src import *

class GunosyNewsTest(unittest.TestCase):

	def test_get_news(self):
	    news = gn.GunosyNews('https://gunosy.com/categories/7')
	    news_list = news.get_news()
	    key_list = list(news_list[0].keys())
	    self.assertTrue(len(news_list) > 10 and key_list[0] == "title" and key_list[1] == "href" and key_list[2] == "time")

if __name__ == '__main__':
	unittest.main()
