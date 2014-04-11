import json
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jpclass.models import Ngrade, Jpclass, Jpclasssubmit
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    if request.method =='POST':
        if request.POST['function'] == 'submit':
            return submit(request)
        if request.POST['function'] == 'clear':
            return clear(request)
    u = request.user
    if Jpclasssubmit.objects.filter(user = u) :
        tempjs = Jpclasssubmit.objects.get(user = u)
    else:
        tempjs = None;
    gradedata = serializers.serialize('json', Ngrade.objects.all())
    classdata = serializers.serialize('json', Jpclass.objects.all())
    context = {'user':request.user, 'user_jpclasssubmit':tempjs, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all(),'gradestr':gradedata,'classstr':classdata}
    return render(request, 'jpclass/index.html', context)

def submit(request):
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
        return HttpResponseRedirect(reverse('jpclass:index'))

def clear(request):
    u = request.user
    if Jpclasssubmit.objects.filter(user = u) :
        Jpclasssubmit.objects.get(user = u).delete()
    return HttpResponseRedirect(reverse('jpclass:index'))

def result(request):
    return render(request, 'jpclass/result.html', {'user':request.user, 'user_jpclasssubmit':Jpclasssubmit.objects.get(user = request.user)})

