from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.models import User


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


def test_make_json(request):
    # python解决方案
    """    import json
    all_data = User.objects.all()
    # json.dumps只识别python常规对象，json.dumps(all_data)会报错
    new_data = []
    for i in all_data:
        _data = {}
        _data['name'] = i.username
        _data['age'] = i.age
        new_data.append(_data)
    json_str = json.dumps(new_data)
    return HttpResponse(json_str,content_type='application/json')"""

    # Django方案1
    # from django.core import serializers
    # qs = User.objects.all()
    # json_str = serializers.serialize('json', qs)
    # return HttpResponse(json_str)

    # Django方案2
    all_data = User.objects.all()
    new_data = []
    for i in all_data:
        _data = {}
        _data['name'] = i.username
        _data['age'] = i.age
        new_data.append(_data)
    return JsonResponse(new_data, safe=False)


def user_index(request):
    return render(request, 'user_index.html')


def test_cross(request):
    return render(request, 'test_cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    return HttpResponse(func + "('wo chuan guo le fang huo qiang come to see you')")


def cross_server_json(request):
    import json
    func = request.GET.get('callback')
    d = {'name': 'gxn', 'age': 18}
    return HttpResponse(func + "(" + json.dumps(d)+")")