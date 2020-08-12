"""
apartments.py

scraper for apartments.com
"""

from bs4 import BeautifulSoup
import requests


class Apartments:

    def __init__(self):

        units = []
        

    def run(self, url):
        _scrape(url)


    def get_units(self):
        return self.units


    def _scrape(self, url):

        r = requests.get(url, headers=default_headers)        
        soup = BeautifulSoup(r.content, 'html.parser')

        soup.prettify()
        #TODO find better way to get hmtl body
        body = list(list(soup.children)[3].children)[3]

        soup.find_all('td', class_='rent')[0]

        soup.find_all('td', class_='
