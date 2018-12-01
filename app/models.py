from django.db import models
import uuid

# Create your models here.
USERNAME_LENGTH=20
ARTICLE_TITLE_LENGTH=20

class User(models.Model):
    #用户id,用户的唯一身份验证,不可重复
    UserID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    #用户名称 不可重复
    UserName = models.CharField(max_length=USERNAME_LENGTH)
    #用户邮箱地址 用于验证?
    Email = models.EmailField()
    #用户密码
    PassWord = models.CharField(max_length=20)
    def __str__(self):
        return self.UserName

class Article(models.Model):
    #文章标题
    Title=models.CharField(max_length=ARTICLE_TITLE_LENGTH)
    #文章作者 一个作者对应多个文章 Django模拟SQL约束ON DELETE CASCADE的行为，并删除包含ForeignKey的对象。
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    #发表时间
    Launch_Time=models.DateTimeField(auto_now_add=True)
    #修改时间 
    Edit_Time=models.DateTimeField(auto_now=True)
    #文章内容
    Content=models.TextField()
    
    def __str__(self):
        return self.Title