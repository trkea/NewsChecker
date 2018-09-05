import unittest
import sys
sys.path.append("../../NewsChecker")
from src import PrtimesNews as pn

class ResponseNewsTest(unittest.TestCase):

	def test_get_news(self):
		news = pn.PrtimesNews("https://prtimes.jp/technology/")
		news_list = news.get_news()
		key_list = list(news_list[1].keys())
		self.assertTrue(len(news_list) > 10 and key_list[0] == "title" and key_list[1] == "href" and key_list[2] == "time")

if __name__ == '__main__':
	unittest.main()