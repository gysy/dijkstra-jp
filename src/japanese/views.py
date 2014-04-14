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
def get_context(request):
    u = request.user
    if Jpclasssubmit.objects.filter(user = u) :
        tempjs = Jpclasssubmit.objects.get(user = u)
    else:
        tempjs = None;
    gradedata = serializers.serialize('json', Ngrade.objects.all())
    classdata = serializers.serialize('json', Jpclass.objects.all())
    context = {'user':request.user, 'user_jpclasssubmit':tempjs, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all(),'gradestr':gradedata,'classstr':classdata,'examdate':Examdate.objects.all(),'signup':Examsignup.objects.all(),'score':Examscore.objects.all()}
    return context

def japanese_index(request):
    if request.method =='POST':
        if request.POST['function'] == 'jpclass_submit':
            return jpclass_submit(request)
        if request.POST['function'] == 'jpclass_clear':
            return jpclass_clear(request)
        if request.POST['function'] == 'signup_submit':
            return signup_submit(request)
        if request.POST['function'] == 'score_submit':
            return score_submit(request)
    else:
        deleteid=request.GET.get("signupdeleteid")
        if deleteid:
            return signup_delete(request,deleteid)
        deleteid=request.GET.get("scoredeleteid")
        if deleteid:
            return score_delete(request,deleteid)

    context = get_context(request)    
    return render(request, 'japanese/index.html', context)

def jpclass_submit(request):
    try:
        #turn received KV into model Jpclass
        tempngrade = Ngrade.objects.get(id = request.POST['ngradeid'])
        tempjpclass = Jpclass.objects.get(id = request.POST['jpclassid'],ngrade = tempngrade )
        context = get_context(request)
    except ObjectDoesNotExist:
        context['error_message']="wrong input."
        return render(request, 'japanese/index.html',context)
    else:
        u = request.user
        if Jpclasssubmit.objects.filter(user = u) :
            Jpclasssubmit.objects.get(user = u).delete()
        #save data
        u.jpclasssubmit_set.create(jpclass = tempjpclass)
        return HttpResponseRedirect(reverse('japanese:japanese_index'))

def jpclass_clear(request):
    u = request.user
    if Jpclasssubmit.objects.filter(user = u) :
        Jpclasssubmit.objects.get(user = u).delete()
    return HttpResponseRedirect(reverse('japanese:japanese_index'))
#signup
def signup_submit(request):
    try:
        ngrade=Ngrade.objects.get(pk = request.POST['grade'])
        date=Examdate.objects.get(pk = request.POST['date'])
        u = request.user
        if Examsignup.objects.filter(user=u,ngrade = ngrade,examdate = date):
            Examsignup.objects.get(user=u,ngrade = ngrade,examdate = date).delete()
    except(ObjectDoesNotExist):
        context = get_context(request)
        context['error_message']="wrong input"
        return render(request, 'japanese/index.html', context)
    else:
        u.examsignup_set.create(ngrade = ngrade, examdate=date)
        return HttpResponseRedirect(reverse('japanese:japanese_index'))

def signup_delete(request,id):
    try:
        tempsignup=Examsignup.objects.get(pk = id,user = request.user)
        Examscore.objects.get(examsignup = tempsignup).delete()
        Examsignup.objects.get(pk = id,user = request.user).delete()
        
    except(ObjectDoesNotExist):
        context = get_context(request)
        context['error_message']="delete failed."
        return render(request, 'japanese/index.html',context)
    else:
        return HttpResponseRedirect(reverse('japanese:japanese_index'))

#score

def score_submit(request):
    try:
        context = get_context(request)
        v = request.POST['vocabulary']
        r = request.POST['reading']
        g = request.POST['grammer']
        tempsignup = Examsignup.objects.get(id=request.POST['signup'])
        if not (v.isdigit() and r.isdigit() and g.isdigit()):
            context['error_message']="You've inputed something wrong."
            return render(request,'japanese/index.html',context)
        tempv=int(v)
        tempr=int(r)
        tempg=int(g)
        if tempv<0 or tempv>100 :
            context['error_message']="Vocabulary_score out of range! "
            return render(request,'japanese/index.html',context)
        if tempr<0 or tempr>100 :
            context['error_message']="Reading_score out of range!"
            return render(request,'japanese/index.html',context)
        if tempg<0 or tempg>100 :
            context['error_message']="Grammer_score out of range!"
            return render(request,'japanese/index.html',context)
        if Examscore.objects.filter(examsignup=tempsignup):
            Examscore.objects.get(examsignup=tempsignup).delete()
    except(ObjectDoesNotExist):
        context['error_message']="ObjectDoesNotExist"
        return render(request,'japanese/index.html',context)
    else:
        tempsignup.examscore_set.create(vocabulary = tempv, reading = tempr, grammer = tempg)
        return HttpResponseRedirect(reverse('japanese:japanese_index'))

def score_delete(request,id):
    try:
        tempsignup=Examsignup.objects.get(pk = id,user = request.user)
        Examscore.objects.get(examsignup = tempsignup).delete()
    except(ObjectDoesNotExist):
        context = get_context(request)
        context['error_message']="delete failed."
        return render(request, 'japanese/index.html',context)
    else:
        return HttpResponseRedirect(reverse('japanese:japanese_index'))