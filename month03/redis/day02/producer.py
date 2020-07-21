import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# 任务类别_收件人_发件人_内容
s = '%s_%s_%s_%s' % ('sendEmail', 'g@tedu.cn', 'w@tedu.cn', 'hahaha')
r.lpush('pyl2',s)
print(r.lrange('pyl2',0,-1))
