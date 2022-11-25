import httpx
from bs4 import BeautifulSoup


def get_pashabank_rates():
    try:
        response = httpx.get('https://www.pashabank.ge/en/exchange-rates')

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'lxml')

        currency = soup.find("div", attrs={"class": 'exchange1'}).find("table")

        currency_rates = [i.text for i in currency.find_all('td')]

        return {'USD': {
            'buy': format(float(currency_rates[4]), ".3f"),
            'sell': format(float(currency_rates[5]), ".3f")
        }, 'EUR': {
            'buy': format(float(currency_rates[7]), ".3f"),
            'sell': format(float(currency_rates[8]), ".3f")
        }}

    except:
        return None
