from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def check_loggin(fn):
    def wrap(request, *args, **kwargs):
        # 检查登录
        if 'username' not in request.session or 'uid' not in request.session:
            # 检查cookies
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                # 肯定没有登录
                return HttpResponseRedirect('/user/login')
            else:
                # 回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)

    return wrap


@check_loggin
def add_view(request):
    # 添加笔记
    return HttpResponse('添加笔记')
