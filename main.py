import json
import time

from dotenv import load_dotenv

from libs.parser.parser import match_best_rates
from libs.providers.redis_provider import set_new_data


def main():
    best_rates = match_best_rates()

    if best_rates:
        set_new_data('USD_buy', json.dumps(best_rates['USD']['buy']), 600)
        set_new_data('USD_sell', json.dumps(best_rates['USD']['sell']), 600)
        set_new_data('EUR_buy', json.dumps(best_rates['EUR']['buy']), 600)
        set_new_data('EUR_sell', json.dumps(best_rates['EUR']['sell']), 600)


if __name__ == "__main__":
    print('|Worker| --> Launching...')
    load_dotenv()

    while True:
        print('|Worker| --> Actions starting...')
        start_time = time.time()
        main()
        endTime = time.time() - start_time
        print("|Worker| --> Completed in " + str(round(endTime, 2)) + " seconds!")
        print('|Worker| --> Waiting for 5 minutes...\n')
        time.sleep(300)
