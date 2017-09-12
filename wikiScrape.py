import requests
import wptools
import json
from bs4 import BeautifulSoup
import wikipedia
from urllib.request import urlopen

def getPage(name):
	baseurl = 'http://en.wikipedia.org/w/api.php'
	my_atts = {
		"action": "opensearch",
		"format": "json",
		"search": name,
		"namespace": "0",
		"limit": "10",
		"utf8": True,
		"formatversion" : 2
	}
	r = requests.get(baseurl, my_atts)
	print(r.status_code)
	#soup = BeautifulSoup(r.content, 'html.parser')


def getSummary(name):
	print(wikipedia.summary(name))

	baseurl = 'http://en.wikipedia.org/w/api.php'
	my_atts = {
		"action": "query",
		"format": "json",
		"titles": name,
		"prop" : "info"
	}


	header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
	r = requests.get(baseurl, headers=header, params = my_atts)
	r = r.json()
	return(r["query"]["pages"].keys()[0])




#f = wptools.page("Ed Sheeran").get_query()
def getArtistInfo(name):
	fela = wptools.page(name).get_parse()
	for info in fela.infobox.keys():
			if info != "image" and info != "labels":
				return(fela.infobox[info])

