from bs4 import BeautifulSoup
import urllib2

url = 'http://pleer.net/search?q=one+dance+drake'

soup = BeautifulSoup(urllib2.urlopen(url), 'html.parser')

song = soup.find(class_='icon download-btn2')

song_url = song.contents[1]['href']

download = BeautifulSoup(urllib2.urlopen(song_url), 'html.parser')

down_link = 

req2 = urllib2.Request(song_url)

response = urllib2.urlopen(req2)

print 'downloading the song....'
data = response.read()
print 'complete downloading, writing file'
song = open('Drake.mp3', "wb")
song.write(data) 
song.close()
