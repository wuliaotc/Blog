from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
# Create your views here.

def home(request):
    return render(request,'app/home.html')


def register(request):
    if request.method=="GET":
        request.session['home'] = request.META.get('HTTP_REFERER', '/') 
        return render(request,'app/work_flex_part01.html')

    elif request.method=="POST":
        UserName=request.POST['USN']#不可重复 需要校验 空格等非法字符
        PassWord=request.POST['PWD']
        Email=request.POST['Email']#不可重复
         
        pass#这里需要加上参数校验


        #判断用户名是否被使用过
        if User.objects.filter(UserName=UserName).exists():
            return HttpResponse("此用户名已被使用")
        if User.objects.filter(Email=Email).exists():
            return HttpResponse("此邮箱已被绑定")
        
        User.objects.create(UserName=UserName,Email=Email,PassWord=PassWord)
        
        return HttpResponse("注册成功")
        #return HttpResponseRedirect(request.session['home']) 

        
def login(request):
    if request.method=="GET":
        return render(request,'app/login.html')

    elif request.method=="POST":
        UserName=request.POST['USN']#不可重复 需要校验 空格等非法字符
        PassWord=request.POST['PWD']


        temp=User.objects.filter(UserName=UserName)
        if not temp.exists():
            return HttpResponse("此用户名不存在")
        elif temp[0].PassWord !=PassWord:
            return HttpResponse("密码错误")
        else:
            return HttpResponse("登陆成功")

        #return HttpResponseRedirect(request.session['home']) 
