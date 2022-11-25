import httpx


def get_mbc_rates():
    try:
        r = httpx.get('https://fxrates.mbc.com.ge:8022/api/fxrates/mbc/commercial')

        if r.status_code != 200:
            return None

        data = r.json()

        resp = {}

        for item in data['FXRates']:
            if item['FromCcy'] == 'USD' and item['ToCcy'] == 'GEL':
                resp['USD'] = {
                    'buy': format(float(item['Buy']), ".3f"),
                    'sell': format(float(item['Sell']), ".3f")
                }

            if item['FromCcy'] == 'EUR' and item['ToCcy'] == 'GEL':
                resp['EUR'] = {
                    'buy': format(float(item['Buy']), ".3f"),
                    'sell': format(float(item['Sell']), ".3f")
                }

        return resp


    except:
        return None
