from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
hobby={'read','sport','game','music'}

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
        
        return HttpResponse(UserName+'<br>'+PassWord+'<br>'+Email)
        #return HttpResponseRedirect(request.session['home']) 

        
def login(request):
    return HttpResponse('咕咕咕')
    


def setting(request):
    if request.method=='GET':
        return render(request,'app/work_flex_part02.html')
    elif request.method=='POST':
        std_Class=request.POST['class']
        std_College=request.POST['college']
        std_Number=request.POST['stdNumber']
        std_genter=request.POST['genter']
        std_hooby=request.POST['hobby']
        remark=request.POST['remark']
        return HttpResponse(std_Class+'<br>'+std_College+'<br>'+std_Number+'<br>'+std_genter+'<br>'+' '.join(std_hooby)+'<br>'+remark)