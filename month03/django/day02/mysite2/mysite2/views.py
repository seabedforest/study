from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def test_html(request):
    # 方案1
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)

    # 方案2
    dic = {}
    dic['str'] = 'guoxiaonao'
    dic['int'] = 8
    dic['lst'] = ['Jack', 'tom', 'Lily']
    dic['dict'] = {'haha': 'hello world'}
    dic['function'] = say_hi
    dic['class'] = Dog()
    dic['script'] = '<script>alert(11)</script>'
    return render(request, 'test_html.html', dic)


def say_hi():
    return 'Hi everyone~~'


class Dog:
    def say(self):
        return "wangwangwang"


def mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST['op']
        print("cal post is ",request.POST)

        if not x or not y:
            return HttpResponse('Please give me number')

        try:
            x=int(x)
            y=int(y)
        except Exception as e:
            print('mycal error is %s' % e)
            return HttpResponse('Please give me number!!')
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            try:
                result = x / y
            except ZeroDivisionError as e:
                return HttpResponse(e)

        return render(request,'mycal.html',locals())