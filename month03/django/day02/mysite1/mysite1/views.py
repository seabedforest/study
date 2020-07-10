from django.http import HttpResponse, HttpResponseRedirect


def page_index_view(request):
    return HttpResponse('这是我的主页页面')


def page_2003_view(request):
    return HttpResponse('这是page2003页面')


def page_1_view(request):
    print('path_info is ', request.path_info)
    print('method is ', request.method)
    print('full path is ', request.get_full_path())
    return HttpResponse('这是编号为1的网页')


def page_2_view(request):
    return HttpResponse('这是编号为2的网页')


def pagen_view(request, pg):
    html = '这是编号%s的网页!!!' % (pg)
    return HttpResponse(html)


def calculate(request, num1, string, num2):
    if string not in ['add', 'sub', 'mul']:
        return HttpResponse('Your string is wrong!!!')
    result = 0
    if string == 'add':
        result = num1 + num2
    elif string == 'sub':
        result = num1 - num2
    elif string == 'mul':
        result = num1 * num2
    return HttpResponse("页面显示结果为:%s" % (result))


def show_birthday(request, year, month, day):
    html = "生日为: %s年%s月%s日" % (year, month, day)
    # return HttpResponse("生日为: %s年%s月%s日" % (year, month, day))
    # 302跳转 参数为  要重定向到的   路由地址 - '/'  开头的相对地址
    return HttpResponseRedirect('/page/1')


#######day02###########
POST_FORM = """
<form method='post' action="/test_get_post">
    姓名:<input type="text" name="username">
    <input type='submit' value='登陆'>
</form>
"""


def test_get_post(request):
    # ?a=100&b=200&c=300&b=400
    # print('query string is',request.GET['b'])
    # print('query string is', request.GET.get('a', 'not data'))
    # print('query string is', request.GET)
    # print('request GET list is', request.GET.getlist('b'))
    # return HttpResponse('--test get post is ok')
    if request.method == 'GET':
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        # 处理POST发来的数据
        value = request.POST.get('username','')
        return HttpResponse('--username is %s' % (value))
