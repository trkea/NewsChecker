import unittest
import sys
sys.path.append('../../NewsChecker')
from src import VehicleNews as vn

class VehicleNewsTest(unittest.TestCase):

	def test_get_news(self):
		news  = vn.VehicleNews('https://trafficnews.jp/category/road')
		news_list = news.get_news()
		key_list = list(news_list[0].keys())
		self.assertTrue(len(news_list) > 5 and key_list[0] == "title" and key_list[1] == "href" and key_list[2] == "time")

if __name__ == '__main__':
    unittest.main()		