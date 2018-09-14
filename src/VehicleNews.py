import urllib.request
from bs4 import BeautifulSoup
import HtmlParser as hp

class VehicleNews():

	def __init__(self,url):
		self.url = url

	def get_news(self):
	    html = hp.HtmlParser.get_html('',url=self.url)
	    div_news = html.find_all("div",class_="post-list-detail")
	    div_time = html.find_all("div",class_="post-list-date")
	    all_list = []
	    for news,time in zip(div_news,div_time):
	        a_tag = news.find("a")
	        title = a_tag.text
	        href =  "https://trafficnews.jp" + a_tag.get("href")
	        time = time.find("time").text
	        news_info = {"title": title, "href": href, "time": time}
	        all_list.append(news_info)
	    return all_list    
