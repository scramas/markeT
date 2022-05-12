import requests
import time
from bs4 import BeautifulSoup
import lxml
url='https://www.proacton.ru/about-internet/terms-glossary'
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}
req = requests.get(url=url, headers=headers)
src = req.text
soup = BeautifulSoup(src, "lxml")
list=[]
cards = soup.find('div', itemprop='articleBody').findAll("p")
with open('it.doc', 'w',encoding='utf-8') as f:
    for dict in cards:
        list.append(dict.text)
with open('it.doc', 'w',encoding='utf-8') as f:
    for i in list:
        file=f.write(i+'\n')
