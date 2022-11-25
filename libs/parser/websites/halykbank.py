import re

import httpx
from bs4 import BeautifulSoup


def get_halykbank_rates():
    try:
        response = httpx.get('https://halykbank.ge/en/individuals/currency')

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'lxml')

        currency = soup.find("div", attrs={"class": 'currencies__tab-content tab-content'}).find("tbody")

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
