from bs4 import BeautifulSoup
import urllib2
import selenium
from selenium import webdriver
import time
import os

url = 'http://www.billboard.com/charts/hot-100'

print "Getting top songs from www.billboard.com\n"
soup = BeautifulSoup(urllib2.urlopen(url), 'html.parser')

songs = soup.findAll(class_='chart-row__title')

song_names = dict()

try:
        
    print 'writing songs on chart'
    open('Billboard Top Songs.txt', 'w').close()	# deleting existing content
    file = open('Billboard Top Songs.txt', 'w')
    count = 1
    for s in songs:
        artist = s.contents[3].string[33:]
        file.write(str(count) + '. ' + s.contents[1].string + ' - ' + artist + '\n')
        if count < 10:
            for a in range(len(artist)):
                if artist[a] == ' ':
                    singer = artist[:a]
                    print singer
                    break
            song_names[s.contents[1].string] = singer
        count +=1

    file.close()
    print 'Succesfully written songs on the text file\n'

except:
    print 'Cannot open text file for writing the songs!\n'

print 'Do you want to download top 10 songs too ? y/n'
inp = raw_input()
if inp == 'y':

    chromedriver = "C:/Python27/Scripts/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    count = 1
    for n in song_names:
        name = list(n)
        for i in range(len(name)):
            if name[i] == ' ':
                name[i] = '+'
        try:
            url = 'http://pleer.net/search?q=' + ''.join(name) + '+' + song_names[n]
            soup = BeautifulSoup(urllib2.urlopen(url), 'html.parser')
            song = soup.find(class_='icon download-btn2')
            song_download_url = 'http://pleer.net' + song.contents[1]['href']

            driver.get(song_download_url)
            download_btn = driver.find_element_by_class_name('download-btn2')
            download_btn.click()    #hopefully starts download
            print 'Download of song %d will start shortly....'%count
        except:
            print 'Some error occured during download.....skipping to next song....'
              
        count +=1
        if count > 10:
            break

    print 'All 10 songs downloaded...'
    driver.close()

elif inp == 'n':
    print 'ok, you can see list opened at the side'
    os.system('notepad.exe Billboard Top Songs.txt')
else:
    print 'invalid input, considering it as no anyway...'
    os.system('notepad.exe Billboard Top Songs.txt')
