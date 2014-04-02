from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from score.models import Examscore
from signup.models import Examsignup

# Create your views here.
def index(request):
    context = {'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)}
    return render(request, 'score/index.html', context)

def result(request):
	tempexamsignup = []
	for signup in Examsignup.objects.filter(user=request.user):
		tempexamsignup.append(Examscore.objects.filter(examsignup=signup))
	return render(request, 'score/result.html', {'user':request.user, 'exam_score':tempexamsignup})

def submit(request):
	try:
	    v = request.POST['vocabulary']
	    r = request.POST['reading']
	    g = request.POST['grammer']
	    tempsignup = Examsignup.objects.get(id=request.POST['signup'])
	    if not (v.isdigit() and r.isdigit() and g.isdigit()):
	    	return render(request,'score/index.html',{ 'error_message':"You've inputed something wrong! Please try again.",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
	    tempv=int(v)
	    tempr=int(r)
	    tempg=int(g)
	    if tempv<0 or tempv>100 :
	    	return render(request,'score/index.html',{ 'error_message':"Vocabulary_score out of range! Please try again.",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
	    if tempr<0 or tempr>100 :
	    	return render(request,'score/index.html',{ 'error_message':"Reading_score out of range! Please try again.",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
	    if tempg<0 or tempg>100 :
	    	return render(request,'score/index.html',{ 'error_message':"Grammer_score out of range! Please try again.",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
	    Examscore.objects.get(examsignup=tempsignup).delete()
	except(KeyError):
		return render(request,'score/index.html',{ 'error_message':"You've inputed something wrong! Please try again.",'user':request.user, 'exam_signup':Examsignup.objects.filter(user = request.user)})
	except(ObjectDoesNotExist):
		tempsignup.examscore_set.create(vocabulary = tempv, reading = tempr, grammer = tempg)
		return HttpResponseRedirect(reverse('score:result'))
	else:
		tempsignup.examscore_set.create(vocabulary = tempv, reading = tempr, grammer = tempg)
		return HttpResponseRedirect(reverse('score:result'))
