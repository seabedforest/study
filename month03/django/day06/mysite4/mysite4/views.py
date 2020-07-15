from django.http import HttpResponse


def test_set_cookies(request):
    resp = HttpResponse('test set cookies is ok')
    # 添加cookie
    # resp.set_cookie('uname', 'guoxiaonao', 300)
    # 删除cookie
    resp.delete_cookie('uname')
    return resp


def test_get_cookies(request):
    # v = request.COOKIES['uname']
    v2 = request.COOKIES.get('uname', 'no data')
    return HttpResponse('Cookies uname is %s' % v2)


def test_set_session(request):
    request.session['uuname'] = 'guoxiaoonao'
    return HttpResponse('set session is ok')


def test_get_session(request):
    v = request.session['uuname']
    return HttpResponse('get session uuname is %s' % v)
