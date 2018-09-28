import unittest
import sys
sys.path.append("../../NewsChecker")
from src import TourismEconomyNews as ten

class TourismEconomyNewsTest(unittest.TestCase):

	def test_get_news(self):
	    news = ten.TourismEconomyNews("https://www.kankokeizai.com/")
	    news_list = news.get_news()
	    key_list = list(news_list[0].keys())
	    self.assertTrue(len(news_list) >= 40 and key_list[0] == "title" and key_list[1] == "href" and key_list[2] == "time") 
	    #news_num = 49
if __name__ == '__main__':
	unittest.main()
