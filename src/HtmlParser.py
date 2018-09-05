import urllib.request
from bs4 import BeautifulSoup

class HtmlParser:
        
	@staticmethod
	def get_html(self,url):
	    html = urllib.request.urlopen(url)
	    soup = BeautifulSoup(html,"html.parser")
	    return soup	
