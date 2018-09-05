from . import HtmlParser as hp

class PrtimesNews:

	def __init__(self,url):
		self.url = url

	def get_news(self):
	    html = hp.HtmlParser.get_html('',url=self.url)  
	    news_list = html.find_all("a", class_="link-thumbnail link-thumbnail-ordinary")
	    date_list = html.find_all("time",class_="time-release time-release-ordinary icon-time-release-svg")
	    all_news = []
	    for news,date in zip(news_list,date_list):
	    	href = news.get("href")
	    	title = news.get("title")
	    	time = date.text.replace("\n","").replace(" ","")
	    	news_info = {"title":title, "href":href, "time":time}
	    	all_news.append(news_info)
	    return all_news

