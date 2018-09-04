import urllib.request
from bs4 import BeautifulSoup

class GunosyNews():

	def __init__(self,url):
		self.url = url


	def get_html(self):
		html = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html,"html.parser")
		return soup

