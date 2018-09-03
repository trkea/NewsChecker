from bottle import get, static_file,route, run,template,request
import feedparser

@route("/")
def index():
    url = 'feed://feeds.japan.zdnet.com/rss/zdnet/all.rdf'
    rss = feedparser.parse(url)

    zdnet_list = []
    for data in rss['entries']:
        value = data['summary_detail']['value'].replace('<p>', '').replace('</p>', '')
        zdnet_list.append([
                           data['updated']
                           , data['title']
                           , data['links'][0]['href']
                           , value[:value.find('<br')]
                           , value[value.find('<img'):].replace('<img src="', '').replace('" /></a>', '')
                           ])

    return template("top",zdnet_list=zdnet_list)

@route("/sample")
def sample():
    return "<h1>Hello world</h1><p> I'm at sample</p><a href='/'>移動する</a>"

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

run(host='localhost', port=8080, debug=True, reloader=True)
