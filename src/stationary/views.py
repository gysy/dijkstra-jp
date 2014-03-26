from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from stationary.models import StationaryType, Choice


# Create your views here.
def index(request):
    context = {'user':request.user,'stationarytype':StationaryType.objects.all()}
    return render(request, 'stationary/index.html', context)

def result(request):
    return render(request,'stationary/result.html',{'user_list':User.objects.all(),'stationary_list':StationaryType.objects.all()})


def submit(request):
    stationary_num=[]
    try:
        for i in range(1,StationaryType.objects.count()+1):
            stationary_num.append(request.POST['stationary_num'+str(i)])
    except (KeyError, StationaryType.DoesNotExist):
        return render(request, 'stationary/index.html',{
            'error_message': "You didn't input all choices.",
           })
    else:
#         choice=Choice(user=request.user,stationary_type=None,num=stationary_num)
#         choice.save()
        u=request.user
        i=0
        for stationarytype in StationaryType.objects.all():
            u.choice_set.create(stationary_type=stationarytype,num=int(stationary_num[i]))
            i=i+1
        return HttpResponseRedirect(reverse('stationary:result'))
    