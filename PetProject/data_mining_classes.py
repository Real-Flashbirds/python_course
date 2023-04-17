import json
import os

from bs4 import BeautifulSoup
import requests




class GDP_data:
    def __init__(self):
        self.url = 'https://pkgstore.datahub.io/core/gdp/gdp_json/data/1a2503aa36368933be8f9a96e1dc16de/gdp_json.json'

    def get_gdp_json(self):
        """
        get the json file from the databank server
        :return: json file containing the global gdp table
        """
        headers = {'Accept': 'application/json'}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"could not get json file from url")
            return response.status_code

    def use_gdp(self, json: dict) -> str:
        """
        parse the json dict and render the data as a table form. You may use HTML <table> tags.
        """
        table = ''
        for country in json:
            name = country['Country Name']
            print(f'The country is {country}')
        return table

class Country_and_region:
    def __init__(self):
        self.file = 'countries.json'

    def read_data(self):
        print(os.getcwd())
        f= open(self.file, encoding="utf8")

        return json.load(f)

    def show_data(self, json) -> str:
        """
        parse the json dict and render the data as a table form. You may use HTML <table> tags.
        """
        table = ''
        for country in json:
            print(f'The country is {country}')
        return table

if __name__ == '__main__':
    countries = Country_and_region()
    countries.show_data(countries.read_data())