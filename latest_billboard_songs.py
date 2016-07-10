from bs4 import BeautifulSoup
import urllib2
import time
import os

url = 'http://www.billboard.com/charts/hot-100'

print "Getting top songs from www.billboard.com\n"
soup = BeautifulSoup(urllib2.urlopen(url), 'html.parser')

songs = soup.findAll(class_='chart-row__title')

try:
        
    print 'writing songs on chart'
    open('Billboard Top Songs.txt', 'w').close()	# deleting existing content
    file = open('Billboard Top Songs.txt', 'w')
    count = 1
    for s in songs:
        artist = s.contents[3].string[33:]
        file.write(str(count) + '. ' + s.contents[1].string + ' - ' + artist + '\n')
        count +=1

    file.close()
    print 'Succesfully written songs on the text file\n'
    os.system('notepad.exe Billboard Top Songs.txt')

except:
    print 'Cannot open text file for writing the songs!\n'


