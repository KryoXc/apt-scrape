#!/usr/bin/env python3

"""
APT SCRAPE
"""

# imports to spreadsheet interface and scraper interface
import scrapers

import sys
import argparse
from urllib.parse import urlparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser('Scrape apartment sites.')
    parser.add_argument('url', metavar='[url]', type=str)

    args = parser.parse_args()

    url = urlparse(args.url)

    # url.netloc keeps domain prefix, maybe strip?
    if url.netloc not in scrapers.available:
        sys.exit('No scrapers available for URL.')

    s = scrapers.get_scraper(url)

    print(s)

    s.run(url)
    
    units = s.get_units()

    for unit in units:
        for field in unit:
            print(field)
        print('\n')

    if len(units) == 0:
        sys.exit('No units found in page.')

    

    # remove duplicates to main data
    # merge with main data
    # upload to google shee
