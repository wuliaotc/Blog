from django.db import models
import uuid

# Create your models here.
USERNAME_LENGTH=20
ARTICLE_TITLE_LENGTH=20

class User(models.Model):
    UserID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    UserName = models.CharField(max_length=USERNAME_LENGTH)
    Email = models.EmailField()

    def __str__(self):
        return self.UserName

class Article(models.Model):
    Title=models.CharField(max_length=ARTICLE_TITLE_LENGTH)
    Author= models.CharField(max_length=USERNAME_LENGTH)
    Launch_Time=models.DateTimeField()
    Content=models.TextField()
    
    def __str__(self):
        return self.Title