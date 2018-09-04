import urllib.request
from bs4 import BeautifulSoup

class GunosyNews():

	def __init__(self,url):
		self.url = url


	def get_html(self):
		html = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html,"html.parser")
		return soup

	def get_news(self):
		html = self.get_html()
		div_news = html.find_all("div",class_="list_title")
		span_times = html.find_all("span",class_="list_desc_media")
		all_news = []
		i = 0
		for div,span in zip(div_news,span_times):
			a_tag = div.find("a")
			text = a_tag.text
			href = a_tag.get('href')
			time = span.text
			news_info ={"title":text, "href":href,"time":time}
			all_news.append(news_info)
		return all_news






