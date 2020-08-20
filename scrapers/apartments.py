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

        unit = ['']

        # figure out if it's a single or multi unit page
        body.find_all(True, {'class': ['availabilityTable',
                                             'multiunit']
                            })
        # find availability table

        # check for availability. tiertwo class? or check for h3 tag.


        

        # Get the Name/Location field
        name = body.find_all('a', class_='neighborhood')[0].text
        unit.append(name)

        # Get the property address, could be in 2 places.
        #address = body.find_all('div', class_='propertyAddress')
        address = body.find_all('h1', class_='propertyName')
        unit.append(address[0].text)

        # second location


        # Get the rent        
        rent = body.find_all('td', class_='rent')
        unit.append(rent[0].text.strip())

        # Get the sqft
        sqft = body.find_all('td', class_='sqft')
        unit.append(sqft[0].text)

        # Get the deposit
        deposit = body.find_all('td', class_='deposit')
        unit.append(deposit[0].text)

        # Parse the bedrooms
        beds = body.find_all('td', class_='beds')

        unit.append('beds')

        # parse utilities
        unit.append('utilities')

        # parse outdoor space
        unit.append('outdoor')        

        # add messaged field
        unit.append('no')

        # add url
        unit.append(url.geturl())

        # add notes area
        unit.append('notes')

        self.units.append(unit)

        return

        # parse features for amenities

        features = body.find_all('div', class_='specList')
        feature_list = []

        for feature in features:
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

    def validate_url(self, url):
        pass
