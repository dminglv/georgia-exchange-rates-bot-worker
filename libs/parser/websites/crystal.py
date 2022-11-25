import httpx
import json


def get_crystal_rates():
    try:
        r = httpx.get('https://crystal.ge/api/wi/rate/v1/cryst?key=52ef35743f3c4f5027d82f051c258241')

        if r.status_code != 200:
            return None

        data = r.json()

        if not data['success']:
            return None

        resp = {}

        parsed_json = json.loads(data['data'])

        for key in parsed_json['data']['CurrencyRate']:
            match key['ISO']:
                case 'USD':
                    resp['USD'] = {
                        'buy': format(float(key['AMOUNT_BUY']), ".3f"),
                        'sell': format(float(key['AMOUNT_SELL']), ".3f")
                    }
                case 'EUR':
                    resp['EUR'] = {
                        'buy': format(float(key['AMOUNT_BUY']), ".3f"),
                        'sell': format(float(key['AMOUNT_SELL']), ".3f")
                    }

        return resp

    except:
        return None
