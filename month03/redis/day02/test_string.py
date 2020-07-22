import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
# string
# r.mset({'pys1': 'ggg', 'pys2': 'aaaa'})
# print(r.mget('pys1', 'pys2', 'pys3'))
# print(r.incr('pys6'))

# hash
# r.hset('pyh1', 'uname', 'wangweichao')
# print(r.hgetall('pyh1'))
# r.hmset('pyh1', {'age': 64, 'desc': 'spider'})
# print(r.hgetall('pyh1'))

# set
# r.sadd('pys1', 'tom', 'jack')
# print(r.smembers('pys1'))
#
# r.sadd('pys2', 'tom', 'lili', 'xixi')
# print(r.sinter('pys1', 'pys2'))

# sorted set
# r.zadd('pyz1', {'tom': 6000, 'jim': 5000})
# print(r.zrange('pyz1', 0, 1, withscores=True))
# print(r.zrangebyscore('pyz1', 4000, 6000, withscores=True))
# print(r.zrangebyscore('pyz1', '(4000', 6000, withscores=True))
# r.zadd('pyz2', {'tom': 8000})
# print(r.zrange('pyz2', 0, -1, withscores=True))
# r.zinterstore('pyz3', ('pyz1', 'pyz2'), aggregate='max')
# print(r.zrange('pyz3', 0, -1, withscores=True))
r.zinterstore('pyz4', {'pyz1': 1, 'pyz2': 0.5}, aggregate='min')
print(r.zrange('pyz4', 0, -1, withscores=True))
