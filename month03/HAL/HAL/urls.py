"""HAL URL Configuration

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
from django.urls import path, include
from goods.views import detail
from cart.views import add_cart, show_cart, remove_cart, place_order, submit_order, submit_success
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/add_cart/', add_cart),  # 添加到购物车
    path('goods/', include('goods.urls')),  # 商品分类页面
    path('cart/show_cart/', show_cart),  # 购物车页面
    path('cart/remove_cart/', remove_cart),  # 购物车删除页面
    path('cart/place_order/', place_order),  # 提交订单页面显示
    path('cart/submit_order/', submit_order),  # 提交订单功能
    path('cart/submit_success/', submit_success),  # 提交订单成功
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
