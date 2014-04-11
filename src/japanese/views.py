import json
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from japanese.models import Ngrade, Jpclass, Jpclasssubmit, Examsignup, Examdate
from japanese.models import Examscore
from django.core.exceptions import ObjectDoesNotExist

#jpclass
def jpclass_index(request):
    if request.method =='POST':
        if request.POST['function'] == 'submit':
            return jpclass_submit(request)
        if request.POST['function'] == 'clear':
            return jpclass_clear(request)
    u = request.user
    if Jpclasssubmit.objects.filter(user = u) :
        tempjs = Jpclasssubmit.objects.get(user = u)
    else:
        tempjs = None;
    gradedata = serializers.serialize('json', Ngrade.objects.all())
    classdata = serializers.serialize('json', Jpclass.objects.all())
    context = {'user':request.user, 'user_jpclasssubmit':tempjs, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all(),'gradestr':gradedata,'classstr':classdata}
    return render(request, 'japanese/index.html', context)

def jpclass_submit(request):
    try:
        #turn received KV into model Jpclass
        tempngrade = Ngrade.objects.get(id = request.POST['ngradeid'])
        tempjpclass = Jpclass.objects.get(id = request.POST['jpclassid'],ngrade = tempngrade )
    except ObjectDoesNotExist:
        return render(request, 'jpclass/index.html',{'error_message':"wrong input.", 'user':request.user, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all()})
    else:
        u = request.user
        if Jpclasssubmit.objects.filter(user = u) :
            Jpclasssubmit.objects.get(user = u).delete()
        #save data
        u.jpclasssubmit_set.create(jpclass = tempjpclass)
        return HttpResponseRedirect(reverse('japanese:jpclass_index'))

def jpclass_clear(request):
    u = request.user
    if Jpclasssubmit.objects.filter(user = u) :
        Jpclasssubmit.objects.get(user = u).delete()
    return HttpResponseRedirect(reverse('japanese:jpclass_index'))
#signup
def signup_index(request):
    context = {'userlist':request.user, 'exam_date':Examdate.objects.all(), 'exam_ngrade':Ngrade.objects.all()}
    return render(request, 'signup/index.html', context)

def signup_result(request):
    return render(request, 'signup/result.html', {'user_list':request.user, 'signup_list':Examsignup.objects.filter(user=request.user)})

def signup_submit(request):
    try:
        ngrade=Ngrade.objects.get(pk = request.POST['grade'])
        date=Examdate.objects.get(pk = request.POST['date'])
        u = request.user
        if Examsignup.objects.filter(user=u,ngrade = ngrade,examdate = date):
            Examsignup.objects.get(user=u,ngrade = ngrade,examdate = date).delete()
    except(ObjectDoesNotExist):
        return render(request, 'signup/result.html', {'error_message':"wrong input.",'user_list':request.user, })
    else:
        u.examsignup_set.create(ngrade = ngrade, examdate=date)
        return HttpResponseRedirect(reverse('japanese:signup_result'))
#score

def score_index(request):
    context = {'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)}
    return render(request, 'score/index.html', context)

def score_result(request):
    tempexamsignup = []
    for signup in Examsignup.objects.filter(user=request.user):
        tempexamsignup.append(Examscore.objects.filter(examsignup=signup))
        return render(request, 'score/result.html', {'user':request.user, 'exam_score':tempexamsignup})

def score_submit(request):
    try:
        v = request.POST['vocabulary']
        r = request.POST['reading']
        g = request.POST['grammer']
        tempsignup = Examsignup.objects.get(id=request.POST['signup'])
        if not (v.isdigit() and r.isdigit() and g.isdigit()):
            return render(request,'score/index.html',{ 'error_message':"You've inputed something wrong! ",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
        tempv=int(v)
        tempr=int(r)
        tempg=int(g)
        if tempv<0 or tempv>100 :
            return render(request,'score/index.html',{ 'error_message':"Vocabulary_score out of range! ",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
        if tempr<0 or tempr>100 :
            return render(request,'score/index.html',{ 'error_message':"Reading_score out of range!",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
        if tempg<0 or tempg>100 :
            return render(request,'score/index.html',{ 'error_message':"Grammer_score out of range!",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
        if Examscore.objects.filter(examsignup=tempsignup):
            Examscore.objects.get(examsignup=tempsignup).delete()
    except(ObjectDoesNotExist):
        return render(request,'score/index.html',{ 'error_message':"ObjectDoesNotExist.",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
    else:
	tempsignup.examscore_set.create(vocabulary = tempv, reading = tempr, grammer = tempg)
	return HttpResponseRedirect(reverse('japanese:score_result'))
