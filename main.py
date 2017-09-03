import requests
import json
from bs4 import BeautifulSoup

base_url = "https://api.genius.com"
headers = { 'Accept' : 'application/json', 'Authorization': 'Bearer tokenhere'}

song_title = "Waves"
artist_name = "Kanye West"

def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
 # print(song_url)
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  page_url = "http://genius.com" + path
 # print(page_url)
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")

  [h.extract() for h in html('script')]
  lyrics = html.find("lyrics").get_text()
  return lyrics


search_url = base_url + "/search"
data = {'q': song_title}
res = requests.get(search_url, data=data, headers=headers)
json = res.json()
print(json)
for hit in json["response"]["hits"]:
    if hit["result"]["primary_artist"]["name"] == artist_name:
      song_info = hit
    if song_info:
        song_api_path = song_info["result"]["api_path"]
        print (lyrics_from_song_api_path(song_api_path))
        break
