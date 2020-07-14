from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bookstore.models import Book


# Create your views here.
def all_book(request):
    books = Book.objects.exclude(is_active=False)
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        print('--get book error %s' % e)
        return HttpResponse('---The book is not existed')
    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        # 获取上传的数据
        price = request.POST['price']
        market_price = request.POST['market_price']
        # 改
        book.price = price
        book.market_price = market_price
        # 保存
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('del get book is error %s' % e)
        return HttpResponse('---The book is not existed')
    book.is_active = False
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')


def create_book(request):
    if request.method == 'GET':
        return render(request, 'bookstore/create_book.html')
    elif request.method == 'POST':
        # 获取上传的数据
        title = request.POST['title']
        pub = request.POST['pub']
        price = request.POST['price']
        market_price = request.POST['market_price']
        # 增加
        Book.objects.create(title=title,pub=pub,price=price,market_price=market_price)
        return HttpResponseRedirect('/bookstore/all_book')