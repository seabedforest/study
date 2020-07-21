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
r.sadd('pys1', 'tom', 'jack')
print(r.smembers('pys1'))

r.sadd('pys2', 'tom', 'lili', 'xixi')
print(r.sinter('pys1', 'pys2'))
