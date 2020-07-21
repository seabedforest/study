import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

while True:
    task = r.brpop('pyl2',10)
    if task:
        task_data = task[1]
        task_str = task_data.decode()
        task_list = task_str.split('_')
        print('----receiver task type is %s'%(task_list[0]))
    else:
        print('---not task ---')