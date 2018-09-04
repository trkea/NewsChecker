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
		all_news = []
		i = 0
		for div in div_news:
			a_tag = div.find("a")
			text = a_tag.text
			href = a_tag.get('href')
			news_info ={"title":text, "href":href}
			all_news.append(news_info)
		return all_news






