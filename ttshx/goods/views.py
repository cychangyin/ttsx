#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from django.http import JsonResponse

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
    context={'list':list1}
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
    context={'page':pagelist,'tid':tid,'type':type,'orderby':orderby,'newlist':newlist}
    return render(request,'goods/list.html',context)


def detail(request,gid):
    #获取要展现的具体商品
    goods=GoodsInfo.objects.get(pk=gid)
    goods.gclick=goods.gclick + 1
    goods.save()
    # 该分类的最新两条数据
    newlist = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={'goods':goods,'newlist':newlist}
    return render(request,'goods/detail.html',context)

