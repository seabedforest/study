import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
# 登录
r.setbit('user_id_login_2020', 4, 1)
