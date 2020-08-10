"""
scrape_test.py

testing flow of beautiful soup with data from requests

"""

import requests
import scrapers
from bs4 import BeautifulSoup

r = requests.get('https://www.apartments.com/1318-n-grant-ave-columbus-oh-unit-207/55y15mp/', headers=scrapers.default_headers)
r2 = requests.get('https://www.apartments.com/the-district-at-tuttle-columbus-oh/bbthwvb/', headers=scrapers.default_headers)
soup = BeautifulSoup(r2.content, 'html.parser')

soup.prettify()
html = list(soup.children)[3]

#print([type(i) for i in list(html.children)])

body = list(html.children)[3]


res = body.find('td', class_='deposit ')

res = soup.find_all('td', class_='rent')[0]

print(res)
print(type(res))
