import re

import httpx
from bs4 import BeautifulSoup


def get_rico_rates():
    try:
        response = httpx.get('https://www.rico.ge')

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'lxml')

        all_rates = soup.find("div", attrs={"class": 'tab-content', "id": "rates-calculator-content"})

        format_rates = [i.text for i in all_rates.find_all('td', attrs={'class': 'h5 font-weight-bold text-primary'})]

        data = []

        for element in format_rates:
            slice = re.sub("^\s+|\n|\r|\s+$", '', element)

            data.append(slice)

        return {'USD': {
            'buy': format(float(data[0]), ".3f"),
            'sell': format(float(data[1]), ".3f")
        }, 'EUR': {
            'buy': format(float(data[2]), ".3f"),
            'sell': format(float(data[3]), ".3f")
        }}

    except:
        return None
