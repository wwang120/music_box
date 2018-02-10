from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import os
option = webdriver.ChromeOptions()
download_dir = "/Users/wanjiewang/PycharmProjects/music_box/music_box/raw_data"
preference = {"download.default_directory": download_dir ,
               "directory_upgrade": True,
               "safebrowsing.enabled": True,
               "extensions":''}
option.add_experimental_option('prefs',preference)
url = 'https://bittigermusicplayerdata.s3-us-west-2.amazonaws.com'
response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html,'lxml')
filenames = soup.find_all('key')
filenames.pop(-1)
count = 0
for filename in filenames:
    download_url = url+ '/'+filename.text
    print('------downloading ' + filename.text + '------')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get(download_url)
    while not os.path.isfile('music_box/raw_data/'+filename.text):
        continue
    browser.quit()
    print('------finish downloading '+filename.text+'------')
    count += 1
print('finish downloading '+str(count)+' files')
