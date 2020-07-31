import hashlib

from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import time, jwt, json
from user.models import UserProfile


# 10200-10299
# Create your views here.


def make_token(username, exp=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now_t = time.time()
    payload = {'username': username, 'exp': now_t + exp}
    return jwt.encode(payload, key, algorithm='HS256')


def token(request):
    """
    创建token 即用户登录
    :param request:
    :return:
    """
    if request.method != 'POST':
        result = {'code': 10200, 'error': 'Please use POST'}
        return JsonResponse(result)

    # 前端地址 5000/login html ->login.html
    # 前端登录成功后 存储token和用户名 弹框 登录成功
    json_str = request.body
    json_obj = json.loads(json_str)
    print(json_str)
    # v1/token
    # 比对密码
    username = json_obj['username']
    password = json_obj['password']
    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        print('---get user error is %s' % e)
        result = {'code': 10201, 'error': 'The username or password is wrong'}
        return JsonResponse(result)

    m = hashlib.md5()
    m.update(password.encode())
    if m.hexdigest() != user.password:
        result = {'code': 10202, 'error': 'The username or password is wrong'}
        return JsonResponse(result)

    # 签发token
    token = make_token(username)

    # return {'code':200,'username':xxx,'data':{'token':xxx}}
    result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
    return JsonResponse(result)
