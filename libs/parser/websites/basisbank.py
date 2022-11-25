import httpx
import json


def get_basisbank_rates():
    try:
        r = httpx.get('https://static.bb.ge/source/api/view/main/getXrates')

        if r.status_code != 200:
            return None

        data = r.json()

        parsed_json = json.loads(data[0]['xrates'])

        return {'USD': {
            'buy': format(float(parsed_json['kursBuy']['USD']), ".3f"),
            'sell': format(float(parsed_json['kursSell']['USD']), ".3f")
        }, 'EUR': {
            'buy': format(float(parsed_json['kursBuy']['EUR']), ".3f"),
            'sell': format(float(parsed_json['kursSell']['USD']), ".3f")
        }}

    except:
        return None