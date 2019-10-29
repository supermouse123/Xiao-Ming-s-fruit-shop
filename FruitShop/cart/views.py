from django.shortcuts import render, HttpResponse
import redis
from home.models import AllGoods
# Create your views here.

r = redis.Redis(host="127.0.0.1", port=6379, db=8)
def index(request):
    username = request.session.get("username")
    if username:
        goods_name = r.hget(username, "goods_name")
        goods_price = r.hget(username, "goods_price")
        goods_number = r.hget(username, "goods_number")
        goods_img = r.hget(username, "goods_img")

    else:
        goods_name = request.session.get("goods_name")
        goods_price = request.session.get("goods_name")
        goods_name = request.session.get("goods_name")

    return render(request, "cart.html")


def select_goods(request):
    if request.is_ajax():
        username = request.session.get("username")
        goods_id = request.GET.get("goods_id")
        goods_number = request.GET.get("number")
        curr_goods = AllGoods.objects.filter(id=goods_id)
        goods_img = curr_goods[0].productimg
        goods_price = curr_goods[0].price
        goods_name = curr_goods[0].productname
        if username:
            r.hmset(username, {goods_id: {"goods_name": goods_name, "goods_price": goods_price,
                              "goods_number": goods_number, "goods_img": goods_img}})
        else:
            goods_dict = {"goods_name": goods_name, "goods_price": goods_price, "goods_number": goods_number,
                          "goods_img": goods_img}
            d = request.session.get("goods_dict")
            if d == None:
                request.session["goods_dict"] = {goods_id: goods_dict}
            else:
                d[goods_id] = goods_dict
                request.session["goods_dict"] = d
        return HttpResponse("success")
    return render(request, "classify.html")

