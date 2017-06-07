#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from ttusers.user_decorator import *
from django.http import HttpResponse,JsonResponse
# Create your views here.

@login
def add(request,gid,count):
    carts = CartInfo.objects.filter(goods_id=gid).filter(user_id=request.session['user_id'])
    if len(carts)==0:
        cart=CartInfo()
        cart.goods_id=int(gid)
        cart.user_id=request.session['user_id']
        cart.count=int(count)
        cart.save()
    else:
        cart=carts[0]
        cart.count+=int(count)
        cart.save()
    if request.is_ajax():
        return JsonResponse({'count':CartInfo.objects.filter(user_id=request.session['user_id']).count()})
    else:
        return redirect('/cart/list/')

@login
def list(request):
    cart_list = CartInfo.objects.filter(user_id=request.session['user_id'])
    context = {
        'title':'购物车',
        'page_name': 1,
        'cart_list': cart_list,
    }
    return render(request, 'cart/cart.html', context)

def count_change(request):
    id = request.GET.get('id')
    count = request.GET.get('count')

    cart=CartInfo.objects.get(id=int(id))
    cart.count=int(count)
    cart.save()
    return JsonResponse({'count':cart.count})

def delete(request):
    id=request.GET.get('id')
    cart = CartInfo.objects.get(id=int(id))
    cart.delete()
    return JsonResponse({'result': 'ok'})