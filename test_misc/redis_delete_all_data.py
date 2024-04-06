import redis
import random
import string

r = redis.Redis(host='localhost', port=6379, db=0)
for key in r.scan_iter():
    r.delete(key)
    print(f'Delete key: {key.decode("utf-8")}')