import spotilib
from bs4 import BeautifulSoup
import urllib.request
import re
#import main
#spotilib.generating(spotilib.artist(), spotilib.song(), save=False)


spotilib.printSong()

def lookupSong(artist, title):
	title = str(title).split('(')[0].strip()
	search = title + " " + artist
	search = search.replace(' ', '+')
	url = "https://genius.com/search?q=" + search
	print(url)

	link = getFirstSearch(url)
	print(link)
	print(type(link))
#	lyrics = main.get_song_lyrics(artist, title)
	#div = getLyrics(link)
	#lyrics = re.findall(r'(.*?)\<.*?\>', div)
#	print(lyrics)

def getLyrics(url):
	soup = getUrl(url)
	tags = soup('div')
	for tag in tags:
		print(tag)
#		if re.match(r'.*<!-- Usage', tag):
#			return tag

def getFirstSearch(url):	
	soup = getUrl(url)
	tags = soup('li')
	for tag in tags:
		if re.match('search_result', tag.get('class', None)):
			return tag.get('href', None)
def getUrl(url):
	with urllib.request.urlopen(url) as url:
  		s = url.read()
	soup = BeautifulSoup(s, 'lxml')	
	soup.prettify().encode("ascii")
	return soup;
#lookupSong(spotilib.artist(), spotilib.song())

