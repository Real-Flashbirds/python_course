import datetime
import random
import time
from Country_GDP.models import FieldGDP, Country, Region, GDP
from data_mining_classes import GDP_data, Country_and_region

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bank_project.Bank.settings")

import django

django.setup()


def populate():
    my_gdp_data = GDP_data()
    gdp_json_data = my_gdp_data.get_gdp_json()
    my_country_data = Country_and_region()
    country_json_data = my_country_data.read_data()
    for data in gdp_json_data:
        the_country = None

        for country in Country.objects.all():
            # We find the country that matched the data
            if country.name == data['Country Name']:
                the_country = country
        if the_country is None:
            # If the country is currently not in the database, we add it
            the_region = None
            flag_unicode = None
            country_code = data['Country Code']
            for countries_and_region in country_json_data:
                if countries_and_region['iso3'] == country_code:
                    flag_unicode = countries_and_region['emojiU']
                    region_name = countries_and_region['region']
                    the_region = None
                    for region in Region.objects.all():
                        if region.name == region_name:
                            the_region = region
                    if the_region is None:
                        # If the region does not exist, we create it
                        new_region = Region(name=region_name)
                        new_region.save()
                        the_region = new_region
            if the_region and flag_unicode:
                country = Country(name=data['Country Name'], abbreviation=data['Country Code'],
                                  region=the_region, flag=flag_unicode)
                country.save()
                the_country = country

        if the_country:
            print("Gdp: ", data['Value'], "   country:  ", the_country)
            my_gdp = GDP(number=data['Value'])
            my_gdp.save()
            field = FieldGDP(GDP=my_gdp, year=data['Year'], country=the_country, population=0)
            field.save()
