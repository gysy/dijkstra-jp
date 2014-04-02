from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jpclass.models import Ngrade, Jpclass, Jpclasssubmit
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    context = {'user':request.user, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all()}
    return render(request, 'jpclass/index.html', context)

def submit(request):
    try:
        #turn received KV into model Jpclass
        tempngrade = Ngrade.objects.get(grade= request.POST['ngrade'])
        tempclassname = request.POST['classname']
        tempjpclass = Jpclass.objects.get(ngrade = tempngrade, classname = str(tempclassname))

#    except (KeyError, Ngrade.DoseNotExist):
#        return render(request, 'jpclass/index.html',{'error_message':"You didn't choose level.", 'user':request.user, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all()})
#    except (KeyError, Jpclass.DoesNotExist):
#        return render(request, 'jpclass/index.html',{'error_message':"level dose not match class.", 'user':request.user, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all()})
    except ObjectDoesNotExist:
        return render(request, 'jpclass/index.html',{'error_message':"wrong input.", 'user':request.user, 'ngrade':Ngrade.objects.all(),'jpclass':Jpclass.objects.all()})
    else:
        u = request.user
        if(Jpclasssubmit.objects.get(user = u) is None):
            Jpclasssubmit.objects.get(user = u).delete()
        #save data
        u.jpclasssubmit_set.create(jpclass = tempjpclass)
        return HttpResponseRedirect(reverse('jpclass:result'))

def result(request):
    return render(request, 'jpclass/result.html', {'user':request.user, 'user_jpclasssubmit':Jpclasssubmit.objects.get(user = request.user)})

