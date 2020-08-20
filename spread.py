"""
spread.py

class interface with google sheets repo
"""

import gspread


class Spread:

    def __init__(self):
        self.gc = gspread.service_account('./service_account.json')
        self.sh = self.gc.open("Apartment Hunt")

    def get_all_sheet_data(self):

        # add cache
        return self.sh.sheet1.get_all_values()

    def post(self, data):
    """data should be a list of values, in order"""
        self.sh.sheet1.append_rows(data)
