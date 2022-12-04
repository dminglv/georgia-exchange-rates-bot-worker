import httpx
from bs4 import BeautifulSoup


def get_mjc_rates():
    try:
        response = httpx.get('http://mjc.ge/')

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'lxml')

        data = []

        for element in soup.find_all("div", {"class": "gw-go-body-cell"}):
            curse = element.find('div', {'class': 'curses'})
            buy_rate = curse.span.text
            sell_rate = curse.span.next_sibling.text
            data.append(buy_rate)
            data.append(sell_rate)

        return {'USD': {
            'buy': format(float(data[0]), ".3f"),
            'sell': format(float(data[1]), ".3f")
        }, 'EUR': {
            'buy': format(float(data[2]), ".3f"),
            'sell': format(float(data[3]), ".3f")
        }}

    except:
        return None
