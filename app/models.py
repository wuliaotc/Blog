from django.db import models
import uuid

# Create your models here.
USERNAME_LENGTH=20
ARTICLE_TITLE_LENGTH=20

class User(models.Model):
    #用户id,用户的唯一身份验证,不可重复
    UserID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    #用户名称 可重复
    UserName = models.CharField(max_length=USERNAME_LENGTH)
    #用户邮箱地址 用于验证?
    Email = models.EmailField()

    def __str__(self):
        return self.UserName

class Article(models.Model):
    #文章标题
    Title=models.CharField(max_length=ARTICLE_TITLE_LENGTH)
    #文章作者 一个作者对应多个文章
    Author=models.ForeignKey(User)
    #发表时间
    Launch_Time=models.DateTimeField(auto_now_add=True)
    #修改时间
    Edit_Time=models.DateTimeField(auto_add=True)
    #文章内容
    Content=models.TextField()
    
    def __str__(self):
        return self.Title