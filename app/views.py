from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from .models import User, Article,childRemark,parentRemark,ArticleLike
import json
import markdown
from app import identity
from Blog import settings
import os
from django.utils import log
from helper import htmlToText
# Create your views here.
# def islogin(func):
#     '''身份认证装饰器，
#     :param func:
#     :return:
#     '''
#     def wrapper(request, *args, **kwargs):
#         if not request.session.get("is_login",False):
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#         return func(request, *args, **kwargs)

#     return wrapper

def toIndex(request):
    return HttpResponseRedirect('/index')

def index(request):
    context = {}
    context['is_login'] = request.session.get('is_login', False)
    context['USN'] = request.session.get('user_name', '')
    context['avator'] = request.session.get('avator','../static/images/default_avater.jpg')
    return render(request, "app/index.html", {'context':context})

# def is_login(request):
#     data_dict = {
#             "is_login": False,
#     }
#     if request.session.get('is_login', False):
#         data_dict = {
#             "is_login": request.session['is_login'],
#             "USN": request.session['user_name']
#         }

#     return JsonResponse(data_dict)

def register(request):
    if request.method == "POST":
        UserName = request.POST['USN']  #不可重复 需要校验 空格等非法字符
        PassWord = request.POST['PWD']
        Email = request.POST['Email']  #不可重复

        pass  #这里需要加上参数校验

        #判断用户名是否被使用过
        if User.objects.filter(UserName=UserName).exists():
            return HttpResponse("此用户名已被使用")
        if User.objects.filter(Email=Email).exists():
            return HttpResponse("此邮箱已被绑定")

        User.objects.create(UserName=UserName, Email=Email, PassWord=PassWord)

        return HttpResponse("注册成功")
        #return HttpResponseRedirect(request.session['home'])

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def login(request):
    if request.method == "POST":
        UserName = request.POST['USN']  #不可重复 需要校验 空格等非法字符
        PassWord = request.POST['PWD']

        request.session['index'] = request.META.get('HTTP_REFERER', '/')
        temp = User.objects.filter(UserName=UserName)
        if not temp.exists():
            return HttpResponse("此用户名不存在")
        elif temp[0].PassWord != PassWord:
            return HttpResponse("密码错误")
        else:#这里代表登陆成功了
            #设置session
            request.session['is_login'] = True
            request.session['user_id'] = temp[0].UserID.__str__()
            request.session['user_name'] = temp[0].UserName
            request.session['avator'] = os.path.join(settings.MEDIA_URL,
                                                 settings.MDEDITOR_CONFIGS['default']['image_folder']+'/',
                                                 temp[0].AvatorFileName)
            print(settings.MEDIA_URL)
            print(settings.MDEDITOR_CONFIGS['default']['image_folder'])
            print(temp[0].AvatorFileName)
            print(request.session['avator'])
            rep=HttpResponseRedirect(request.session['index'])
            rep.set_cookie('usn', temp[0].UserName)#记得加密!
            return rep
            #return HttpResponseRedirect(request.session['index'])
            '''if 'k' in request.COOKIES:
                pass
                return HttpResponse('2')
            else:
                rep=HttpResponseRedirect(request.session['index'])
                rep.set_cookie('k','v')
            return rep'''

        #return HttpResponseRedirect(request.session['home'])
@identity.islogin
def ChangePassword(request):
    if request.method=="POST":
        UserName = request.session['user_name']
        PassWord = request.POST['PWD']  #不可重复 需要校验 空格等非法字符
        rePassWord = request.POST['rePWD']
        if(PassWord==rePassWord):#在服务器验证密码相同
            # 验证密码强度 还没写
            u= User.objects.get(UserName=UserName)
            u.PassWord=PassWord
            u.save()
            request.session.flush() #logout
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponse('密码不匹配')
    return HttpResponse('未知错误')




def GetArticleList(request):
    if request.method == "POST":
        start = int(request.POST['start'])
        num = int(request.POST['num'])
        obj_dict_list=list()
        s_code = 0  #成功的情况下
        msg = 'SUCCESS'

        for obj in Article.objects.filter(id__gte=start,id__lt=start+num):
            content=str(obj.Content)
            content=markdown.markdown(
                    str(obj.Content),
                     extensions=[
                        'markdown.extensions.extra',
                        'markdown.extensions.codehilite',
                        'markdown.extensions.toc',
                    ])
            content=htmlToText.dehtml(content)
            if len(content)>50:
                content=content[0:50]+"......"
            obj_dict=dict(
                id=str(obj.id),
                Title = str(obj.Title),
                Author = str(obj.Author),
                Launch_Time = str(obj.Launch_Time),
                Content = content,
                LikeCount=obj.LikeCount,
                ViewCount=obj.ViewCount

            )
            obj_dict_list.append(obj_dict)

        data_dict = dict(
            status=s_code,
            msg=msg,
            num=len(obj_dict_list),
            Article=obj_dict_list
        )
        return JsonResponse(data_dict)
    #这里的内容给缩略版 小于50字

# {
#     "status":"0",
#     "msg":
#     "SUCCESS",
#     "Article": [{
#         "id": "123",
#         "Author": "123",
#         "Launch_Time": "123",

#         "Content": "123"
#     },
#     {
#         "Title": "123",
#         "Author": "123",
#         "Launch_Time": "123",
#         "Edit_Time": "123",
#         "Content": "123"
#     }]
# }

def GetArticleData(request, article_id):
    article_obj = Article.objects.filter(
        id=str(article_id))[0]  #需要判断是否存在 还没写!!

    s_code = 0  #成功的情况下
    msg = 'SUCCESS'
    Title = str(article_obj.Title)
    Author = str(article_obj.Author)
    Launch_Time = str(article_obj.Launch_Time)
    Edit_Time = str(article_obj.Edit_Time)
    Content = str(article_obj.Content)
    if request.method == "GET":
        data_str = "{status:" + str(
            s_code
        ) + ",msg:" + msg + ",Title:" + Title + ",Author:" + Author + ",Launch_Time:" + Launch_Time + ",Edit_Time:" + Edit_Time + ",Content:" + Content + "}"
        return HttpResponse(data_str)
    elif request.method == "POST":
        data_dict = dict(
            status=s_code,
            msg=msg,
            Title=Title,
            Author=Author,
            Launch_Time=Launch_Time,
            Edit_Time=Edit_Time,
            Content=Content)

        return JsonResponse(data_dict)
        #render(request,"app/home.html",json.dumps(data_dict))
        '''
        #{
            "status" : 0 ,          //执行状态码
            "msg"    : "SUCCESS",   //说明文字信息，没有为NULL
            "Title"  :"123",
            "Author" :"123",    
            "Launch_Time":"123",
            "Edit_Time":"123",
            "Content":"123"
        }
        '''


@identity.islogin
def writeblog(request):
    if request.method=="GET":
        return render(request,"app/editor.html")
    elif request.method=="POST":
        title=request.POST.get("title",None)
        content=request.POST.get("content",None)
        if(title and content):#成功运行这个
            Article.objects.create(
                Title=title,
                #文章作者 一个作者对应多个文章 Django模拟SQL约束ON DELETE CASCADE的行为，并删除包含ForeignKey的对象。
                Author=User.objects.get(UserName=request.session['user_name']),
                #文章内容
                Content=content)
            data_dict=dict(
                success= 1,
                message = "success!",
                #url     : "图片地址"
            )
        else:
            data_dict=dict(
                    success= 0,
                    message = "failed!",
                    #url     : "图片地址"
                )
        return JsonResponse(data_dict)

@identity.islogin
def addRemark(request,article_id):#0表示评论失败 不刷新页面 1评论成功 刷新页面
    if request.method =="POST":
        article_obj = Article.objects.filter(
            id=str(article_id))[0]  #需要判断是否存在 还没写!!
        parentRemark.objects.create(
            Article=article_obj,
            Author=User.objects.get(UserName=request.session['user_name']),
            Content=request.POST['remark']
        )
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})


def ShowArticle(request, article_id):
    article_obj = Article.objects.filter(
        id=str(article_id))  #需要判断是否存在 还没写!!
    article_obj.update(ViewCount=article_obj[0].ViewCount+1)
    article_obj=article_obj[0]
    article_obj.ViewCount=article_obj.ViewCount+1
    Author = str(article_obj.Author)
    context = {}
    
    context['article_title'] = str(article_obj.Title)
    context['article_content'] = markdown.markdown(
        str(article_obj.Content),
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    context['LikeCount']=article_obj.LikeCount
    context['ViewCount']=article_obj.ViewCount+1
    
    premarks=[]
    for pr in article_obj.parentRemark.all().order_by('id'):#开始遍历父评论
        pr_dict=dict(
            author=pr.Author.UserName,
            content=pr.Content,
            id=pr.id
        )
        cr_list=[]
        for cr in pr.childRemark.all().order_by('id'):#遍历子评论
            cr_dict = dict(
                replyTo=cr.ReplyTo.UserName,
                author=cr.Author.UserName,
                content=cr.Content,
                id=cr.id
            )
            cr_list.append(cr_dict)
        pr_dict['crs']=cr_list
        premarks.append(pr_dict)

    context['is_login'] = request.session.get('is_login', False)
    context['USN'] = request.session.get('user_name', '')
    context['avator'] = request.session.get('avator','../static/images/default_avater.jpg')
    return render(
        request, "app/article.html", {
            'context':context,
            'premarks': premarks
            #[{
            #     'author': '1',
            #     'content': '2'
            # }, {
            #     'author': '1',
            #     'content': '2'
            # }]
        })

@identity.islogin
def addReply(request,article_id,remark_id):#增加评论
    if request.method == "POST":
        article_obj = Article.objects.filter(
            id=str(article_id))[0]  #需要判断是否存在 还没写!!
        pr_obj = parentRemark.objects.get(
            id=str(remark_id))
        childRemark.objects.create(
            Article=article_obj,
            ParentRemark=pr_obj,
            ReplyTo=pr_obj.Author,
            Author=User.objects.get(UserName=request.session['user_name']),
            Content=request.POST['reply'])
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})



@identity.islogin
def likeArticle(request,article_id):
    if request.method=="GET":
        user=User.objects.filter(UserName=request.session['user_name'])
        article_obj = Article.objects.filter(
            id=str(article_id))  #需要判断是否存在 还没写!!
        if ArticleLike.objects.filter(User=user[0],Article=article_obj[0]):
            return JsonResponse({"status":0})
        ArticleLike.objects.create(User=user[0],Article=article_obj[0])
        article_obj.update(LikeCount=article_obj[0].LikeCount+1)
        return JsonResponse({"status":1})


@identity.islogin
def showUserInfo(request):#渲染用户中心
    if request.method=="GET":
        u=User.objects.get(UserName=request.session['user_name'])
        articles=[]
        for article in u.article.all().order_by('id'):
            articles.append(dict(
                article_id=article.id,
                article_title=article.Title
            ))
        context={}

        context['avator'] = request.session.get('avator','../static/images/default_avater.jpg')
        context['is_login'] = request.session.get('is_login', False)
        context['USN'] = request.session.get('user_name', '')

        return render(request, 'app/info.html',{'context':context,'articles':articles})

def delArticle(request,article_id):#删除文章
    if request.method=="GET":
        Article.objects.get(id=article_id).delete()
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})
