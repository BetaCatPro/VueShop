"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
import xadmin

from mxonline.settings import MEDIA_ROOT
from goods.views import GoodsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ueditor', include('DjangoUeditor.urls')),
    path('docs/', include_docs_urls(title='生鲜')),
    url(r'^api-auth/', include('rest_framework.urls'))

    path('goods/', GoodsListView.as_view(), name='goods-list'),

    path('media/(?p<path>.*)', serve, {'document_root': MEDIA_ROOT})
]
