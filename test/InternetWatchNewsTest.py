import unittest
import sys
sys.path.append("../../NewsChecker")
from src import InternetWatchNews as iwn

class RbbTodayNewsTest(unittest.TestCase):

	def test_get_news(self):
	    news = iwn.InternetWatchNews("https://internet.watch.impress.co.jp/category/topic/index.html")
	    news_list = news.get_news()
	    key_list = list(news_list[0].keys())
	    self.assertTrue(len(news_list) >= 40 and key_list[0] == "title" and key_list[1] == "href" and key_list[2] == "time")

if __name__ == '__main__':
	unittest.main()
