import os
import time
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@cache_page(60)
def test_cache(request):
    time.sleep(3)
    t1 = time.time()
    return HttpResponse('t1 is %s' % t1)


def test_mw(request):
    print('----view in -----')
    return HttpResponse('----test mw is ok')


def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---post is ok')


def test_page(request):
    bks = ['a', 'b', 'c', 'd', 'e', 'f']
    paginator = Paginator(bks, 2)
    cur_page = request.GET.get('page', 1)  # 得到默认的当前页
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())


@csrf_exempt
def upload_view(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == "POST":
        a_file = request.FILES['myfile']
        print("上传文件名是:", a_file.name)
        filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        with open(filename, 'wb') as f:
            data = a_file.file.read()
            f.write(data)
        return HttpResponse("接收文件:" + a_file.name + "成功")
