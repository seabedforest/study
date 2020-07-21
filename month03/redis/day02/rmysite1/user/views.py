from django.http import HttpResponse
from django.shortcuts import render
import redis
from .models import User

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')


# Create your views here.
def user_detail(request, user_id):
    # 优先查缓存
    cache_key = 'user:%s' % (user_id)
    if r.exists(cache_key):
        # 缓存存在
        data = r.hgetall(cache_key)
        new_data = {k.decode(): v.decode() for k, v in data.items()}
        username = new_data['username']
        desc = new_data['desc']
        html = 'cache username is %s desc is %s' % (username, desc)
        return HttpResponse(html)
    else:
        # 无缓存
        try:
            user = User.objects.get(id=user_id)
        except Exception as e:
            print('---get error is %s' % (e))
            return HttpResponse('----no user ----')

        username = user.username
        desc = user.desc
        html = 'username is %s desc is %s' % (username, desc)
        # 存储缓存
        r.hmset(cache_key, {'username': username, 'desc': desc})
        r.expire(cache_key, 60)
        return HttpResponse(html)


def user_update(request, user_id):
    desc = request.GET.get('desc', '')
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        print('---get error is %s' % (e))
        return HttpResponse('----no user ----')
    user.desc = desc
    user.save()

    # 删除缓存
    cache_key = 'user:%s' % (user_id)
    r.delete(cache_key)
    return HttpResponse('---update is ok ---')
