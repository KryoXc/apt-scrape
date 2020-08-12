"""
scrapers/__init__.py
"""

from .apartments import Apartments
from .rent import Rent

available = ['apartments.com', 'rent.com']

default_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def get_scraper(url):
    
    if url.netloc == 'apartments.com':
        return Apartments()
    elif url.netloc == 'rent.com':
        return Rent()
