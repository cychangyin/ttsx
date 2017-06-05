#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
from . import user_decorator
# Create your views here.

def index(request):
    return render(request,'ttusers/index.html')

def register(request):
    return render(request,'ttusers/register.html')
def post1(request):
    dict1=request.POST
    uname=dict1.get('user_name')
    upasswd=dict1.get('pwd')
    upasswd1=dict1.get('cpwd')
    uemail=dict1.get('email')
    if upasswd != upasswd1:
        return redirect('/user/register/')
    else:
        per=UserInfo()
        per.uname=uname
        mysha = sha1()
        mysha.update(upasswd)
        pwd2=mysha.hexdigest()
        per.upasswd=pwd2
        per.uemail=uemail
        per.save()
        return redirect('/user/login/')

def post2(request):
    name = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=name).count()
    return JsonResponse({'count':count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request,'ttusers/login.html',context)

def post3(request):
    pp=request.POST
    name=pp.get('username')
    password=pp.get('pwd')
    jizhu=pp.get('jizhu',0)
    users=UserInfo.objects.filter(uname=name)

    if len(users)==1:
        mysha = sha1()
        mysha.update(password)
        pwd2 = mysha.hexdigest()
        if pwd2==users[0].upasswd:
            print '读取cookie'
            print request.COOKIES
            url=request.COOKIES.get('url','/')
            red=HttpResponseRedirect(url)
            red.set_cookie('url','',max_age=-1)
            if jizhu != 0:
                red.set_cookie('uname',name)
            else:
                red.set_cookie('url','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=name
            return red
        else:
            context = {'error_name': 0, 'error_pwd': 1, 'username': name, 'pwd': password}
            return render(request, 'ttusers/login.html', context)
    else:
        context = {'error_name': 1, 'error_pwd': 0, 'username': name, 'pwd': password}
        return render(request, 'ttusers/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    goods_list = []
    context = {
               'user_email': user_email,
               'user_name': request.session['user_name'],
               'page_name': 1,
               'goods_list': goods_list}
    return render(request,'ttusers/user_center_info.html',context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddrees = post.get('uaddress')
        user.upostalcode = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'user': user,
               'page_name': 1}
    return render(request, 'ttusers/user_center_site.html', context)

@user_decorator.login
def order(request):
    return render(request,'ttusers/user_center_order.html')