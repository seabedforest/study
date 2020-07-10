"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/page/2003
    path('page/2003', views.page_2003_view),
    # http://127.0.0.1:8000/
    path('', views.page_index_view),
    # http://127.0.0.1:8000/page/1
    path('page/1', views.page_1_view),
    # http://127.0.0.1:8000/page/2
    path('page/2', views.page_2_view),
    # http://127.0.0.1:8000/page/3~n
    path('page/<int:pg>', views.pagen_view),
    path('<int:num1>/<str:string>/<int:num2>', views.calculate),
    # http://127.0.0.1:8000/birthday/年/月/日
    re_path(r'^brithday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$',
            views.show_birthday),
    # http://127.0.0.1:8000/birthday/月/日/年
    re_path(r'^brithday/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})$',
            views.show_birthday),

    ###day02###
    # http://127.0.0.1:8000/test_get_post
    path('test_get_post',views.test_get_post)
]
