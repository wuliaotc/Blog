from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request,'app/home.html')


def register(request):
    if request.method=="GET":
        request.session['home'] = request.META.get('HTTP_REFERER', '/') 
        return render(request,'app/work_flex_part01.html')

    elif request.method=="POST":
        UserName=request.POST['USN']
        PassWord=request.POST['PWD']
        Email=request.POST['Email']

        return HttpResponseRedirect(request.session['home']) 

        
def login(request):
    return HttpResponse('咕咕咕')
    


def setting(request):
    
    return HttpResponse('')
    