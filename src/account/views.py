from django.contrib.auth import authenticate,login as user_login, logout as user_logout 
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def index(request):  
  
    return render(request, 'account/login.html')  

def login(request):  
 
    if request.user.is_authenticated():  
        return  HttpResponse('You have logend in.')  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(username=username, password=password)  
        if user is not None:  
            if user.is_active:  
                        user_login(request, user)  
#                         return HttpResponseRedirect('/account/%d' % user.id)  
                        return HttpResponseRedirect(reverse('score:index'))
            else:  
                    return HttpResponse('User might be not invoked!')  
        else:  
                return HttpResponse('Username or Password might be wrong!')  
    else:  
        return render(request,'account/login.html')  

def logout(request):  
    user_logout(request)  
    return render(request,'account/login.html')  
