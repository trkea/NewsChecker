import unittest
import sys
sys.path.append("../../NewsChecker")
from src import TravelVoiceNews as tvn

class TravelVoiceNewsTest(unittest.TestCase):

	def test_get_news(self):
	    news = tvn.TravelVoiceNews("https://www.travelvoice.jp/")
	    news_list = news.get_news()
	    key_list = list(news_list[0].keys())
	    self.assertTrue(len(news_list) >= 10 and key_list[0] == "title" and key_list[1] == "href" and key_list[2] == "time")

if __name__ == '__main__':
	unittest.main()
