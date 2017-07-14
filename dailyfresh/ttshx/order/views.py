#coding=utf-8
from django.shortcuts import render,redirect
from django.db import transaction
from datetime import datetime
from django.http import HttpResponse
from models import *
from ttusers.models import *
from cart.models import *
# Create your views here.
def list(request):
    user=UserInfo.objects.get(id=request.session.get('user_id'))
    cart_ids=request.GET.getlist('carts_id')
    carts_list= CartInfo.objects.filter(id__in=cart_ids)
    context={
            'title':'提交订单',
            'page_name':1,
            'user':user,
            'carts':carts_list,
    }
    return render(request,'order/list.html',context)


'''
1、判断库存
2、减少库存
3、创建订单对象
4、创建详单对象
5、删除购物车
对于以上操作，应该使用事务
问题是：在django的模型类中如何使用事务？

未实现功能：
    真实支付
    物流跟踪
'''

def handle(request):
    post=request.POST
    address=post.get('address')
    cart_ids=post.getlist('carts_id')
    sid=transaction.savepoint()
    try:
        order=OrderInfo()
        uid=request.session['user_id']
        now=datetime.now()
        order.user_id=uid
        order.odate=now
        order.oaddress=address
        order.ototal=0
        order.save()
        total=0
        for cid in cart_ids:
            ocart=CartInfo.objects.get(pk=cid)
            if ocart.goods.gkuncun>=ocart.count:
                #库存足够，允许购买，
                ocart.goods.gkuncun-=ocart.count
                ocart.goods.save()
                #将信息加入详单
                detail=OrderDetailInfo()
                detail.goods=ocart.goods
                detail.order=order
                detail.price=ocart.goods.tprice
                detail.count=ocart.count
                detail.save()
                total+=ocart.goods.tprice*ocart.count
                ocart.delete()

            else:
                transaction.savepoint_rollback(sid)
                return redirect('/cart/')
        order.oIsPay=True
        order.ototal=total
        order.save()
        transaction.savepoint_commit(sid)
        return redirect('/user/order/')
    except:
        transaction.savepoint_rollback(sid)
        return redirect('/cart/')
    return HttpResponse('ok')
