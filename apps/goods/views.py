from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle

#缓存（内存级别）
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Goods, GoodsCategory, HotSearchWords, Banner
from .filters import GoodsFilter
from .serializers import GoodsSerializer, CategorySerializer, HotWordsSerializer, BannerSerializer
from .serializers import IndexCategorySerializer

# Create your views here.


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    商品列表页, 分页， 搜索， 过滤， 排序
    """
    throttle_classes = (UserRateThrottle, )
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('shop_price',)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')
    # ^name开头匹配
    # =name完全匹配
    # name$表示以什么结尾

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchsViewset(mixins.ListModelMixin, GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


class BannerViewset(mixins.ListModelMixin, GenericViewSet):
    """
    轮播图
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer
