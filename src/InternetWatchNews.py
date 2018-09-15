import urllib.request
from bs4 import BeautifulSoup
import HtmlParser as hp

class InternetWatchNews():

	def __init__(self,url):
		self.url = url

	def get_news(self):
		html = hp.HtmlParser.get_html("",url=self.url)
		p_title_list = html.find_all("p",class_="title")
		p_date_list = html.find_all("p", class_="date")
		all_news = []
		del p_title_list[0:8]
		del p_date_list[0:8]
		for p_title_tag, p_date_tag in zip(p_title_list, p_date_list):
			title = p_title_tag.text
			href =  p_title_tag.find("a").get("href")
			time = p_date_tag.text
			not_news = title.find("た日") > -1
			cm = time.find("(") == -1 and time.find(")") == -1
			if(not_news or cm):
				continue
			news_info = {"title": title, "href": href, "time": time}
			all_news.append(news_info)
		return all_news






