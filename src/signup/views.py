from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from signup.models import Examsignup,Examdate
from jpclass.models import Ngrade


# Create your views here.
def index(request):
    context = {'userlist':request.user, 'exam_signup':Examdate.objects.all(),'ngrade':Ngrade.objects.all()}
    return render(request, 'signup/index.html', context)

def result(request):
    return render(request, 'signup/result.html', {'user_list':User.objects.all(), 'signup_list':Examsignup.objects.all()})

def submit(request):
    
    #context = {'userlist':request.user, 'exam_signup':Examsignup.objects.all(),'ngrade':Ngrade.objects.all()}
    #return render(request, 'signup/index.html', context)
    return HttpResponseRedirect(reverse('signup:index'))