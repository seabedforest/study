from django.http import HttpResponse
from django.shortcuts import render


def page_index_view(request):
    return HttpResponse('这是我的主页页面')


def page_2003_view(request):
    return HttpResponse('这是page2003页面')


def page_1_view(request):
    print('path_info is ',request.path_info)
    print('method is ',request.method)
    print('full path is ',request.get_full_path())
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
    return HttpResponse("生日为: %s年%s月%s日" % (year, month, day))

