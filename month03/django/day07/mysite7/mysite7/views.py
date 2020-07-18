import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60)
def test_cache(request):
    time.sleep(3)
    t1= time.time()
    return  HttpResponse('t1 is %s' % t1)

def test_mw(request):
    print('----view in -----')
    return HttpResponse('----test mw is ok')

def test_csrf(request):
    if request.method == 'GET':
        return render(request,'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---post is ok')


