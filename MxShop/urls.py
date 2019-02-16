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

import xadmin
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from MxShop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView


router = DefaultRouter()
#配置goods的url
router.register(r'v1/api/goods', GoodsListViewSet, base_name="goods")
router.register(r'v1/api/categorys', CategoryViewset, base_name="categorys")
router.register(r'v1/api/codes', SmsCodeViewset, base_name="codes")
router.register(r'v1/api/hotsearchs', HotSearchsViewset, base_name="hotsearchs")
router.register(r'v1/api/users', UserViewset, base_name="users")
#收藏
router.register(r'v1/api/userfavs', UserFavViewset, base_name="userfavs")
#留言
router.register(r'v1/api/messages', LeavingMessageViewset, base_name="messages")
#收货地址
router.register(r'v1/api/address', AddressViewset, base_name="address")
#购物车url
router.register(r'v1/api/shopcarts', ShoppingCartViewset, base_name="shopcarts")
#订单相关url
router.register(r'v1/api/orders', OrderViewset, base_name="orders")
"""
#轮播图url
router.register(r'v1/api/banners', BannerViewset, base_name="banners")
#首页商品系列数据
router.register(r'v1/api/indexgoods', IndexCategoryViewset, base_name="indexgoods")

# good_list = GoodsListViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path(r'docs/', include_docs_urls(title="生鲜")),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # drf自带的token认证模式，弊端:token永久有效
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    re_path(r'^login/', obtain_jwt_token),

    # path('goods/', good_list, name='goods-list'),
    path('', include(router.urls)),
    path('alipay/return/', AlipayView.as_view(), name='alipay')

    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
