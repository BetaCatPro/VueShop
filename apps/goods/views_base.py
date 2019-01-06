from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):

    def get(self, request):
        import json
        json_list = []
        goods = Goods.object.all()[:10]
        # 1.0原始方法
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        # 2.0model_to_dict方法
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        # 3.0序列化, （上面的方法都不能序列化datetime，image等）
        from django.core import serializers
        json_data = serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        # return HttpResponse(json.dumps(json_list), content_type='application/json')
        return JsonResponse(json_data, safe=False)
