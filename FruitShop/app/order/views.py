from django.db import transaction
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.generic import View
from goods.models import GoodsSKU
from user.models import Address
from order.models import OrderInfo, OrderGoods

from utils.mixin import LoginRequiredMixin
from django_redis import get_redis_connection
from datetime import datetime

# Create your views here.


class OrderPlaceView(LoginRequiredMixin, View):
    """提交订单页面显示"""
    def post(self, request):
        user = request.user
        sku_ids = request.POST.getlist('sku_ids')
        if not sku_ids:
            return redirect(reverse('cart:show'))

        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id
        skus = []
        total_count = 0
        total_price = 0
        for sku_id in sku_ids:
            sku = GoodsSKU.objects.get(id=sku_id)
            count = conn.hget(cart_key, sku_id)
            amount = sku.price * int(count)
            sku.count = count
            sku.amount = amount
            skus.append(sku)
            total_count += int(count)
            total_price += amount

        #运费
        transit_price = 10
        total_pay = total_price + transit_price

        #地址
        addrs = Address.objects.filter(user=user)

        sku_ids = ','.join(sku_ids)

        context = {
            'skus': skus,
            'total_count': total_count,
            'total_pay': total_pay,
            'total_price': total_price,
            'transit_price': transit_price,
            'addrs': addrs,
            'sku_ids': sku_ids}

        return render(request, 'place_order.html', context)


class OrderCommitView(View):
    """订单创建"""
    def post(self, request):
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        addr_id = request.POST.get('addr_id')
        pay_method = request.POST.get('pay_method')
        sku_ids = request.POST.get('sku_ids')

        if not all([addr_id, pay_method, sku_ids]):
            return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

        if pay_method not in OrderInfo.PAY_METHODS.keys():
            return JsonResponse({'res': 2, 'errmsg': '非法支付方式'})

        try:
            addr = Address.objects.get(id=addr_id)
        except Address.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '地址非法'})

        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)
        transit_price = 10

        total_count = 0
        total_price = 0
        save_id = transaction.savepoint()
        order = OrderInfo.objects.create(order_id=order_id, user=user,
                                         addr=addr, pay_method=pay_method,
                                         total_count=total_count, total_price=transit_price,
                                         transit_price=transit_price)
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id
        sku_ids = sku_ids.split(',')
        for sku_id in sku_ids:
            for i in range(3):
                try:
                    sku = GoodsSKU.objects.get(id=sku_id)
                except:
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'res': 4, 'errmsg': '商品不存在'})

                count = conn.hget(cart_key, sku_id)

                if int(count) > sku.stock:
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'res': 6, 'errmsg': '商品库存不足'})

                #乐观锁判断库存
                orgin_stock = sku.stock
                new_stock = orgin_stock - int(count)
                new_sales = sku.sales + int(count)
                res = GoodsSKU.objects.filter(id=sku_id, stock=orgin_stock).update(stock=new_stock, sales=new_sales)
                if res == 0:
                    if i == 2:
                        transaction.savepoint_rollback(save_id)
                        return JsonResponse({'res': 7, 'errmsg': '下单失败'})
                    continue
                OrderGoods.objects.create(order=order, sku=sku,
                                          count=count, price=sku.price)

                sku.stock -= int(count)
                sku.sales += int(count)
                amount = sku.price * int(count)
                total_count += int(count)
                total_price += amount

                break

            order.total_count = total_count
            order.total_price = total_price
            order.save()

            conn.hdel(cart_key, *sku_ids)

            return JsonResponse({'res': 5, 'msg': '创建成功'})

