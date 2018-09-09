from bottle import get, static_file,route, run,template,request
import requests
import GunosyNews as gn
import PrtimesNews as pn
import VehicleNews as vn

GUNOSY = "Gunosy"
VEHICLE = "Vehicle"
PRTIMES = "Prtimes"


@route("/")
def index():
	news_list = ["Gunosyニュース IT・科学", "乗り物ニュース", "Prtimes"]
	name_list = [GUNOSY,VEHICLE,PRTIMES]
	return template("top", name_list=name_list,news_list=news_list)


global news
@route("/news_list")
def news_list():
	select = request.GET.get("name")
	name = ""
	if select == GUNOSY:
		news = gn.GunosyNews("https://gunosy.com/categories/7")
	if select == VEHICLE:
	    news = vn.VehicleNews("https://trafficnews.jp/category/road")
	if select == PRTIMES:
	    news = pn.PrtimesNews("https://prtimes.jp/technology/")   	
	news_list = news.get_news()
	return template("news_list", news_list=news_list, name=select)


@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host='localhost', port=8080, debug=True, reloader=True)


