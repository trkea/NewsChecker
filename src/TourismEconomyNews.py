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
        all_news = []
        i = 0
        category = ["観光行政","トラベル"]
        for div_tag,ul_tag in zip(div_news,ul_times):
            title = div_tag.find("a").text
            href = div_tag.find("a").get("href")
            time = ul_tag.find("li").text
            if title.find("【PR】") != -1:
                continue
            news_info = {"title": title, "href": href, "time": time}
            all_news.append(news_info)   
        all_news.pop(0)    
        return all_news
