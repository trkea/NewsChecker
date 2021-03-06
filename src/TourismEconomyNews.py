import urllib.request
from bs4 import BeautifulSoup
import  HtmlParser as hp

class TourismEconomyNews():
    def __init__(self,url):
        self.url = url

    def get_news(self):
        html = hp.HtmlParser.get_html("",url=self.url)
        div_news = html.find_all("div",class_="article-content")
        ul_times = html.find_all("ul",class_="list-attributes")
        i = 0
        travel = [8,9,10,11]
        business = [16,17,18,19]
        tourism = [20,21,22,23]
        inbound = [24,25,26,27]
        topic = [40,41,42,43]
        all_news = []
        for div_tag,ul_tag in zip(div_news,ul_times):
            if not(i in travel or i in business or i in tourism or  i in inbound or i in topic):
                i += 1
                continue
            title = div_tag.find("a").text
            if title.find("【PR】") != -1:
                i += 1
                continue  
            href = div_tag.find("a").get("href")
            time = ul_tag.find("li").text
            news_info = {"title": title, "href": href, "time": time}
            all_news.append(news_info)
            i += 1      
        return all_news
