"""
APT SCRAPE
"""

#imports to spreadsheet interface and scraper interface
import scrapers

import sys, argparse
from urllib.parse import urlparse


from enum import Enum


class fields(Enum):
    na = 0
    name = 1
    address = 2
    price = 3
    sqft = 4
    deposit = 5
    beds = 6
    utilities = 7
    outdoor = 8
    messaged = 9
    link = 10
    notes = 11



if __name__ == "__main__":

    parser = argparse.ArgumentParser('Scrape apartment sites.')
    parser.add_argument('url', metavar='[url]', type=str)

    args = parser.parse_args()


    url = urlparse(args.url)

    if url.netloc not in scrapers.available:
        sys.exit('No scrapers available for URL.')

    s = scrapers.get_scraper(url)

    print(s)
    
    s.run()
    
    
    # remove duplicates to main data
    # merge with main data
    # upload to google shee
