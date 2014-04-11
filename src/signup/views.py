from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, loader

from jpclass.models import Ngrade
from signup.models import Examsignup, Examdate, ExamsignupSubmit


# Create your views here.
def index(request):
    context = {'userlist':request.user, 'exam_date':Examdate.objects.all(), 'exam_ngrade':Ngrade.objects.all()}
    return render(request, 'signup/index.html', context)

def result(request):
    return render(request, 'signup/result.html', {'user_list':request.user, 'signup_list':ExamsignupSubmit.objects.filter(user=request.user)})

def submit(request):
    try:
        tempngrade = request.POST['grade']
        tempdate = request.POST['date']
        ngrade=Ngrade.objects.get(grade= tempngrade)
        date=Examdate.objects.get(date=tempdate)
        tempsignup = Examsignup.objects.get(ngrade=ngrade, examdate=date)
        u = request.user
        ExamsignupSubmit.objects.get(examsignup=tempsignup,user=u).delete()
    except(ObjectDoesNotExist):
        u.examsignupsubmit_set.create(examsignup=tempsignup)
        return HttpResponseRedirect(reverse('signup:result'))
    else:
        u.examsignupsubmit_set.create(examsignup=tempsignup)
        return HttpResponseRedirect(reverse('signup:result'))
