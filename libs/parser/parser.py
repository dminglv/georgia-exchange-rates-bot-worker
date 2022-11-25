import os
import time

from libs.parser.websites.basisbank import get_basisbank_rates
from libs.parser.websites.credobank import get_credo_rates
from libs.parser.websites.crystal import get_crystal_rates
from libs.parser.websites.halykbank import get_halykbank_rates
from libs.parser.websites.mbc import get_mbc_rates
from libs.parser.websites.pashabank import get_pashabank_rates
from libs.parser.websites.rico import get_rico_rates
from libs.parser.websites.valuto import get_valuto_rates


def _get_rates():
    rates = {}

    print('Get rates from Credo...')
    start_time = time.time()
    credo_rates = get_credo_rates()
    if not credo_rates:
        print('Error getting results...')

    if credo_rates:
        rates['credo'] = credo_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    print('Get rates from Crystal...')
    start_time = time.time()
    crystal_rates = get_crystal_rates()
    if not crystal_rates:
        print('Error getting results...')

    if crystal_rates:
        rates['crystal'] = crystal_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    print('Get rates from Rico...')
    start_time = time.time()
    rico_rates = get_rico_rates()
    if not rico_rates:
        print('Error getting results...')

    if rico_rates:
        rates['rico'] = rico_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    print('Get rates from Valuto...')
    start_time = time.time()
    valuto_rates = get_valuto_rates()
    if not valuto_rates:
        print('Error getting results...')

    if valuto_rates:
        rates['valuto'] = valuto_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    print('Get rates from MBC...')
    start_time = time.time()
    mbc_rates = get_mbc_rates()
    if not mbc_rates:
        print('Error getting results...')

    if mbc_rates:
        rates['mbc'] = mbc_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    print('Get rates from PASHA Bank...')
    start_time = time.time()
    pashabank_rates = get_pashabank_rates()
    if not pashabank_rates:
        print('Error getting results...')

    if pashabank_rates:
        rates['pashabank'] = pashabank_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    print('Get rates from Halyk bank...')
    start_time = time.time()
    halykbank_rates = get_halykbank_rates()
    if not halykbank_rates:
        print('Error getting results...')

    if halykbank_rates:
        rates['halykbank'] = halykbank_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    print('Get rates from Basis Bank...')
    start_time = time.time()
    basisbank_rates = get_basisbank_rates()
    if not basisbank_rates:
        print('Error getting results...')

    if basisbank_rates:
        rates['basisbank'] = basisbank_rates
        endTime = time.time() - start_time
        print('Done. Completed in ' + str(round(endTime, 2)) + " seconds!")

    return rates


def match_best_rates():
    all_rates = _get_rates()

    all_rates_by_currency_and_type = {
        'USD': {
            'buy': {},
            'sell': {},
        },
        'EUR': {
            'buy': {},
            'sell': {}
        }
    }

    for organization in all_rates:
        all_rates_by_currency_and_type['USD']['buy'][organization] = float(all_rates[organization]['USD']['buy'])
        all_rates_by_currency_and_type['USD']['sell'][organization] = float(all_rates[organization]['USD']['sell'])
        all_rates_by_currency_and_type['EUR']['buy'][organization] = float(all_rates[organization]['EUR']['buy'])
        all_rates_by_currency_and_type['EUR']['sell'][organization] = float(all_rates[organization]['EUR']['sell'])

    sorted_items = sorted(all_rates_by_currency_and_type['USD']['buy'].items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_items)
    all_rates_by_currency_and_type['USD']['buy'] = converted_dict

    sorted_items = sorted(all_rates_by_currency_and_type['EUR']['buy'].items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_items)
    all_rates_by_currency_and_type['EUR']['buy'] = converted_dict

    sorted_items = sorted(all_rates_by_currency_and_type['USD']['sell'].items(), key=lambda x: x[1])
    converted_dict = dict(sorted_items)
    all_rates_by_currency_and_type['USD']['sell'] = converted_dict

    sorted_items = sorted(all_rates_by_currency_and_type['EUR']['sell'].items(), key=lambda x: x[1])
    converted_dict = dict(sorted_items)
    all_rates_by_currency_and_type['EUR']['sell'] = converted_dict

    os.environ['TZ'] = 'Asia/Tbilisi'
    time.tzset()

    return {
        'USD': {
            'buy': {
                'organization': list(all_rates_by_currency_and_type['USD']['buy'].keys())[0],
                'rate': all_rates_by_currency_and_type['USD']['buy'][list(all_rates_by_currency_and_type['USD']['buy'].keys())[0]],
                'updated_time': time.strftime('%b %d %Y %H:%M')
            },
            'sell': {
                'organization': list(all_rates_by_currency_and_type['USD']['sell'].keys())[0],
                'rate': all_rates_by_currency_and_type['USD']['sell'][list(all_rates_by_currency_and_type['USD']['sell'].keys())[0]],
                'updated_time': time.strftime('%b %d %Y %H:%M')
            }
        },
        'EUR': {
            'buy': {
                'organization': list(all_rates_by_currency_and_type['EUR']['buy'].keys())[0],
                'rate': all_rates_by_currency_and_type['EUR']['buy'][list(all_rates_by_currency_and_type['EUR']['buy'].keys())[0]],
                'updated_time': time.strftime('%b %d %Y %H:%M')
            },
            'sell': {
                'organization': list(all_rates_by_currency_and_type['EUR']['sell'].keys())[0],
                'rate': all_rates_by_currency_and_type['EUR']['sell'][list(all_rates_by_currency_and_type['EUR']['sell'].keys())[0]],
                'updated_time': time.strftime('%b %d %Y %H:%M')
            }
        }
    }


def match_organization_name(shortname: str):
    match shortname:
        case 'credo':
            return 'Credo Bank'
        case 'crystal':
            return 'Crystal'
        case 'mbc':
            return 'Micro Bussiness Capital'
        case 'rico':
            return 'Rico Credit'
        case 'valuto':
            return 'Valuto'
        case 'pashabank':
            return 'PASHA Bank'
        case 'halykbank':
            return 'Halyk Bank'
        case 'basisbank':
            return 'BasisBank'