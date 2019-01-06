from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from .models import Goods, GoodsCategory, HotSearchWords, Banner
from .serializers import GoodsSerializer, CategorySerializer, HotWordsSerializer, BannerSerializer

# Create your views here.


