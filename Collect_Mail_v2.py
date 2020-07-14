# -*- coding: UTF-8 -*-
import os
from bs4 import BeautifulSoup
import threading
import requests
from time import sleep
pyPath, filename = os.path.split(__file__)

url = "https://posterspy.com/artists/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
NameList = soup.find_all('a',class_="name")
print(len(NameList))
MailList = soup.find_all('a',class_="btn btn-small btn-primary")
print(len(MailList))

# print(soup)
# print(soup.find_all('a',class_="btn btn-small btn-primary"))
for x, person in enumerate(NameList):
    print(x)
    print(NameList[x].text)
    print(MailList[x].get('href'))