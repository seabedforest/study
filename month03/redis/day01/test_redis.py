import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=1, password='123456')
key_list = r.keys('*')
print(key_list)
print(r.exists('k2'))

# list
r.lpush('pyl1', 'a', 'b', 'c', 'd')
print(r.lrange('pyl1', 0, -1))
