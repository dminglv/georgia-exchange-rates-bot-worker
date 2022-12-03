import re

import httpx
from bs4 import BeautifulSoup


def get_swisscapital_rates():
    try:
        response = httpx.get('https://swisscapital.ge/en/currency')

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'lxml')

        currency = soup.find("tbody")

        currency_rates = [i.text for i in currency.find_all('td')]

        data = []

        for element in currency_rates:
            slice = re.sub("^\s+|\n|\r|\s+$", '', element)

            data.append(slice)

        return {'USD': {
            'buy': format(float(data[1]), ".3f"),
            'sell': format(float(data[2]), ".3f")
        }, 'EUR': {
            'buy': format(float(data[4]), ".3f"),
            'sell': format(float(data[5]), ".3f")
        }}

    except:
        return None


get_swisscapital_rates()