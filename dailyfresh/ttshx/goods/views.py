#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from cart.models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    typelist=TypeInfo.objects.all()
    list1=[]
    for type in typelist:
        list1.append({
            'type': type,
            'click_list': type.goodsinfo_set.order_by('-gclick')[0:3],
            'new_list': type.goodsinfo_set.order_by('-id')[0:4]
        })
    context={'title':'首页','list':list1,'cart_count':cart_count(request)}
    return render(request,'goods/index.html',context)

def list(request,tid,pid,orderby):

    #根据分类查出总数据
    type = TypeInfo.objects.get(pk=int(tid))
    # 拿到最新的2条数据
    newlist =type.goodsinfo_set.order_by('-id')[0:2]
    goodslist=GoodsInfo.objects.filter(gtype_id=int(tid))
    #根据排序方式得到排序后的数据
    if orderby=='1':
        goodslist=goodslist.order_by('-id')
    elif orderby=='2':
        goodslist=goodslist.order_by('-tprice')
    elif orderby=='3':
        goodslist=goodslist.order_by('-gclick')
    p=Paginator(goodslist,10)
    pagelist=p.page(int(pid))
    context={'title':'列表页',
             'page':pagelist,
             'tid':tid,
             'type':type,
             'orderby':orderby,
             'newlist':newlist,
             'cart_count':cart_count(request)
             }
    return render(request,'goods/list.html',context)


def detail(request,gid):
    #获取要展现的具体商品
    goods=GoodsInfo.objects.get(pk=gid)
    goods.gclick=goods.gclick + 1
    goods.save()
    # 该分类的最新两条数据
    newlist = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={'title':'商品详情','goods':goods,'newlist':newlist,'cart_count':cart_count(request)}
    response=render(request,'goods/detail.html',context)
    #保存用户浏览商品信息
    liulan = request.COOKIES.get('liulan','')
    if liulan == '':
        #如果之前没有浏览过，就直接添加cookie
        response.set_cookie('liulan', gid)
    else:
        #如果之前有浏览记录，把浏览记录放在一个列表里
        liulan_list=liulan.split(',')
        #遍历列表，看最新的浏览是否重复，如果重复，删掉旧的，把最新的插入到最前面
        if gid in liulan_list:
            liulan_list.remove(gid)
        liulan_list.insert(0,gid)
        #设置只存5条记录，多余的从最旧的开始删掉。
        if len(liulan_list)>5:
            liulan_list.pop()
        #构造最新的浏览记录，放置在cookie里
        liulan2=','.join(liulan_list)
        response.set_cookie('liulan',liulan2)
    return response

from haystack.views import SearchView
class MySearchView(SearchView):
    def extra_context(self):
        extra=super(MySearchView,self).extra_context()
        extra['title']=self.request.GET.get('q')
        extra['cart_count']=cart_count(self.request)
        return extra



def cart_count(request):
    if request.session.has_key('user_id'):
        return CartInfo.objects.filter(user_id=request.session['user_id']).count()
    else:
        return 0