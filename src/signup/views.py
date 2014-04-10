from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, loader

from jpclass.models import Ngrade
from signup.models import Examdate, Examsignup


# Create your views here.
def index(request):
    context = {'user':request.user, 'exam_date':Examdate.objects.all(), 'exam_ngrade':Ngrade.objects.all()}
    return render(request, 'signup/index.html', context)

def result(request):
    return render(request, 'signup/result.html', {'user':request.user, 'signup_list':Examsignup.objects.filter(user=request.user)})

def submit(request):
    try:
        ngrade = Ngrade.objects.get(id=request.POST['grade'])
        date = Examdate.objects.get(id=request.POST['date'])        
        if Examsignup.objects.get(ngrade = ngrade, examdate=date, user = request.user) :
            return render(request, 'signup/index.html', {'user':request.user, 'exam_date':Examdate.objects.all(), 'exam_ngrade':Ngrade.objects.all(), 'error_message':"You have already signed up this exam!"})
    except(ObjectDoesNotExist):
        request.user.examsignup_set.create(examdate=date, ngrade = ngrade,user = request.user)
        return HttpResponseRedirect(reverse('signup:result'))
    else:
        request.user.examsignup_set.create(ngrade = ngrade, examdate=date, user = request.user)
        return HttpResponseRedirect(reverse('signup:result'))

def cancel(request):
    context = {'user':request.user, 'exam_signup':Examsignup.objects.filter(user=request.user) }
    return render(request, 'signup/cancel.html', context)

def submitc(request):
    try:
        examsignup=Examsignup.objects.get(id=request.POST['examsignupinfo'])
    except(ObjectDoesNotExist):
        return render(request, 'signup/cancel.html', {'user':request.user, 'exam_signup':Examsignup.objects.filter(user=request.user) , 'error_message':"You haven't signed up this exam!"})
    else:
        examsignup.delete()
        return render(request,'signup/result.html',{'user':request.user, 'signup_list':Examsignup.objects.filter(user=request.user),'error_message':"Cancel success"})

def resultall(request):
    return render(request, 'signup/resultall.html', {'user':request.user, 'signup_list':Examsignup.objects.all()})
