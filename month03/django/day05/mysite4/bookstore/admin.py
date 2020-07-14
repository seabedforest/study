from django.contrib import admin
from bookstore import models


# Register your models here.
class BookManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['id', 'title', 'pub', 'market_price']
    # 规定列表页中 点击哪个字段可以进入详情页
    list_display_links = ['title']
    # 过滤器组件
    list_filter = ['pub']
    # 搜索框组件
    search_fields = ['title', 'pub']
    # 可直接在列表页中编辑修改
    list_editable = ['market_price']


class AuthorManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['id', 'name', 'age', 'email']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name', 'email']
    list_editable = ['email']


admin.site.register(models.Book, BookManager)
admin.site.register(models.Author, AuthorManager)
