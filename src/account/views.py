#-*- coding: UTF-8 -*-
from django.contrib.auth import authenticate,login as user_login, logout as user_logout 
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def index(request):  
    # 用户的个人页面  
    return render(request, 'account/login.html')  

def login(request):  
    # 表单提交过来的数据  
    if request.user.is_authenticated():  
        return  HttpResponse('你已经登录')  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(username=username, password=password)  
        if user is not None:  
            if user.is_active:  
                        user_login(request, user)  
#                         return HttpResponseRedirect('/account/%d' % user.id)  
                        return HttpResponseRedirect(reverse('stationary:index'))
            else:  
                    return HttpResponse('用户没有启用!')  
        else:  
                return HttpResponse('用户名或者密码错误！')  
    else:  
        return render(request,'account/login.html')  

def logout(request):  
    user_logout(request)  
    return render(request,'account/login.html')  