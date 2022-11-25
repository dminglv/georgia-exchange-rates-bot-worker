import os
import redis
from dotenv import load_dotenv

load_dotenv()
r = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0,
                ssl=False, ssl_cert_reqs=None, password=os.getenv('REDIS_PASS'), decode_responses=True)


def get_key_data(key):
    return r.get(key)


def delete_by_key(key):
    return r.delete(key)


def set_new_data(key, value, ttl=None):
    return r.set(key, value, ex=ttl)
