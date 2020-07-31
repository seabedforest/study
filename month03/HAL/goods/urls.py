from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),  # 主页
    path('detail', views.detail, name='detail'),  # 详情页
]
