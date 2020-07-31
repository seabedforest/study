from celery import Celery

# 初始化celery, 指定broker
app = Celery('guoxiaonao', broker='redis://:123456@127.0.0.1:6379/1')


# 创建任务函数
@app.task
def task_test():
    print("task is running....")
