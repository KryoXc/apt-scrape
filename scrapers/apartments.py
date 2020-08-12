"""
apartments.py

scraper for apartments.com
"""

from bs4 import BeautifulSoup
import requests


class ApartmentsScraper:

    def __init__(self, headers=None):

        self.units = []
        self.headers = headers

    def run(self, url):
        self._scrape(url)

    def get_units(self):
        return self.units

    def _scrape(self, url):

        r = requests.get(url.geturl(), headers=self.headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        soup.prettify()
        # TODO find better way to get hmtl body
        body = list(list(soup.children)[3].children)[3]

        print(body.find_all('td', class_='rent')[0])
        print(body.find_all('td', class_='sqft')[0])
        print(body.find_all('td', class_='deposit')[0])

        # TODO parse beds and baths

        print(body.find_all('a', class_='neighborhood')[0])
        print('\n')

        features = body.find_all('div', class_='specList')
        feature_list = []


        for feature in features:
            print(feature)
            print('\n')
            if not feature.find_all('li'):
                feature_str = feature.find_all(
                    'span')[-1].text.replace('\r\n', '').replace('\u2022', '').strip()
                if feature_str != '':
                    feature_list.append(feature_str)
            else:
                for li in feature.find_all('li'):
                    feature_str = li.text.replace('\u2022', '')
                    if feature_str != '':
                        feature_list.append(feature_str)

        print(feature_list)
