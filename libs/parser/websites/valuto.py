import httpx


def get_valuto_rates():
    try:
        r = httpx.get('http://valuto.ge/wp-json/rest-currency-list/v3/currencies')

        if r.status_code != 200:
            return None

        data = r.json()

        if not int(data['data']['status']) != '200':
            return None

        return {'USD': {
            'buy': format(float(data['data']['currencies']['USDGEL']['buy']), ".3f"),
            'sell': format(float(data['data']['currencies']['USDGEL']['sell']), ".3f")
        }, 'EUR': {
            'buy': format(float(data['data']['currencies']['EURGEL']['buy']), ".3f"),
            'sell': format(float(data['data']['currencies']['EURGEL']['sell']), ".3f")
        }}


    except:
        return None
