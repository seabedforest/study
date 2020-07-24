from django.http import HttpResponse
from django.shortcuts import render


def test_xhr(request):
    return render(request, 'test_xhr.html')


def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')


def test_xhr_get_server(request):
    return HttpResponse('This is ajax')


def test_get_p(request):
    return render(request, 'test_get_p.html')


def test_get_p_server(request):
    uname = request.GET.get('uname')
    return HttpResponse('欢迎 %s' % uname)


def test_xhr_post(request):
    return render(request, 'test_xhr_post.html')


def test_xhr_post_server(request):
    return HttpResponse('post is ok')


def test_jq_get(request):
    return render(request, 'test_jp_get.html')


def test_jq_get_server(request):
    return HttpResponse('This is jq ajax')


def test_json(request):
    return render(request, 'test_json.html')
