import requests
import wptools
import json
from bs4 import BeautifulSoup
import wikipedia
from urllib.request import urlopen

# # baseurl = 'http://en.wikipedia.org/w/api.php'
# # my_atts = {
# # 	"action": "opensearch",
# # 	"format": "json",
# # 	"search": "Ed Sheeran",
# # 	"namespace": "0",
# # 	"limit": "10",
# # 	"utf8": True,
# # 	"formatversion" : 2
# # }
# # r = requests.get(baseurl, my_atts)
# # print(r.status_code)
# # #soup = BeautifulSoup(r.content, 'html.parser')

# import wikipedia
# print (wikipedia.summary("Wikipedia"))

# baseurl = 'http://en.wikipedia.org/w/api.php'
# my_atts = {
# 	"action": "query",
# 	"format": "json",
# 	"titles": "Ed Sheeran",
# 	"prop" : "info"
# }


# header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
# r = requests.get(baseurl, headers=header, params = my_atts)
# r = r.json()
# print(r["query"]["pages"].keys()[0])




#f = wptools.page("Ed Sheeran").get_query()
fela = wptools.page('Ed Sheeran').get_parse()
for info in fela.infobox.keys():
		if info != "image" and info != "labels":
			print(fela.infobox[info])
#print(f.extext)
