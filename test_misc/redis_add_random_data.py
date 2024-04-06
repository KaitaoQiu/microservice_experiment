import redis
import random
import string

r = redis.Redis(host='localhost', port=6379, db=0)

def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

for i in range(400000):
    key = random_string(30)
    value = random_string(10)
    r.set(key, value)
    print(f'Add key: {key} value: {value}')
