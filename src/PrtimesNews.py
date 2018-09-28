import HtmlParser as hp

class PrtimesNews:

	def __init__(self,url):
		self.url = url

	def get_news(self):
	    html = hp.HtmlParser.get_html('',url=self.url)  
	    a_list = html.find_all("a", class_="link-thumbnail link-thumbnail-ordinary")
	    time_list = html.find_all("time",class_="time-release time-release-ordinary icon-time-release-svg")
	    all_news = []
	    for a_tag,time_tag in zip(a_list,time_list):
	    	href = "https://prtimes.jp" + a_tag.get("href")
	    	title = a_tag.get("title")
	    	time = time_tag.text.replace("\n","").replace(" ","")
	    	news_info = {"title": title, "href": href, "time": time}
	    	all_news.append(news_info)
	    return all_news
