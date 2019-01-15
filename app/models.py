from django.db import models
import uuid
from mdeditor.fields import MDTextField  #必须导入

# Create your models here.
USERNAME_LENGTH=20
ARTICLE_TITLE_LENGTH=20

class User(models.Model):

    #用户id,用户的唯一身份验证,不可重复
    UserID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    #用户名称 不可重复
    UserName = models.CharField(max_length=USERNAME_LENGTH, unique=True)
    #用户邮箱地址 用于验证?
    Email = models.EmailField()
    #用户密码
    PassWord = models.CharField(max_length=256)

    def __str__(self):
        return self.UserName

class Article(models.Model):
    #文章标题
    Title=models.CharField(max_length=ARTICLE_TITLE_LENGTH)
    #文章作者 一个作者对应多个文章 Django模拟SQL约束ON DELETE CASCADE的行为，并删除包含ForeignKey的对象。
    #在这种情况下,如果删除user 就会删除对应的article
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    #发表时间
    Launch_Time=models.DateTimeField(auto_now_add=True)
    #修改时间
    Edit_Time=models.DateTimeField(auto_now=True)
    #文章内容
    Content=MDTextField()

    def __str__(self):
        return self.Title

class  parentRemark(models.Model):#第一级评论
    #id 主键

    #文章 多个评论对应一个文章
    Article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name="parentRemark")

    #是否一级评论 false为二级评论 是回复
    #is_reply=models.BooleanField(default=True)
    #评论组id
    #
    #作者
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myRemark')
    #发表时间
    Launch_Time=models.DateTimeField(auto_now_add=True)
    #修改时间
    Edit_Time=models.DateTimeField(auto_now=True)
    #评论内容
    Content = models.CharField(max_length=256)


class childRemark(models.Model):
    #id 主键

    #文章 多个评论对应一个文章
    Article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="childRemark")

    #父评论
    ParentRemark = models.ForeignKey(
        parentRemark, on_delete=models.CASCADE, related_name="childRemark")

    #是否一级评论 false为二级评论 是回复
    #is_reply=models.BooleanField(default=True)
    #评论组id
    #
    #回复对象
    ReplyTo =models.ForeignKey(
        User, on_delete=models.CASCADE)
    #评论作者
    Author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='myReply')
    #发表时间
    Launch_Time = models.DateTimeField(auto_now_add=True)
    #修改时间
    Edit_Time = models.DateTimeField(auto_now=True)
    #评论内容
    Content = models.CharField(max_length=256)
