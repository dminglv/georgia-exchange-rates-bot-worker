import httpx
from bs4 import BeautifulSoup


def get_credo_rates():
    try:
        response = httpx.get('https://credobank.ge/exchange-rates/?rate=credo')

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'lxml')

        usd = soup.find("div", attrs={"class": 'currency-rate-box', "data-currency": "USD"}).find('ul', attrs={
            'data-type': 'credo'})

        usd_values = [i.text for i in usd.find_all('span', attrs={'class': 'rate-value'})]

        eur = soup.find("div", attrs={"class": 'currency-rate-box', "data-currency": "EUR"}).find('ul', attrs={
            'data-type': 'credo'})

        eur_values = [i.text for i in eur.find_all('span', attrs={'class': 'rate-value'})]

        return {'USD': {
            'buy': format(float(usd_values[0]), ".3f"),
            'sell': format(float(usd_values[1]), ".3f")
        }, 'EUR': {
            'buy': format(float(eur_values[0]), ".3f"),
            'sell': format(float(eur_values[1]), ".3f")
        }}

    except:
        return None
