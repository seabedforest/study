"""mysite7 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from test_upload import views as upload_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_cache', views.test_cache),
    path('test_mw', views.test_mw),
    path('test_csrf', views.test_csrf),

    ####day08###
    path('test_page',views.test_page,name='tp'),
    path('test_upload',views.upload_view),
    path('test_upload_dj',upload_view.upload_view_dj),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
