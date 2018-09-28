import urllib.request
from bs4 import BeautifulSoup
import  HtmlParser as hp

class TravelVoiceNews():

	def __init__(self,url):
		self.url = url

	def get_news(self):
		html = hp.HtmlParser.get_html("", url=self.url)
		div_list = html.find_all("div", class_="news-box js-heighitem-newentry")
		span_list = html.find_all("span", class_="entry-date")
		ul_list = html.find_all("ul", class_="newsbox-list")
		all_news = []
		for li_tag in ul_list[0].find_all("li"):
			title = li_tag.find("a").get("title").replace(" ", "")
			href = li_tag.find("a").get("href")
			time = li_tag.find("span").text.replace(" ", "")
			news_info = {"title": title, "href": href, "time": time}
			all_news.append(news_info)
		return all_news
