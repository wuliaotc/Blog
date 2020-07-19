from django.contrib import admin
from .models import User,Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display=['Title','Author','Launch_Time','Edit_Time',"ViewCount","LikeCount"]
    list_filter = ['Author',"Launch_Time","ViewCount","LikeCount"]

admin.site.register(User)
admin.site.register(Article,ArticleAdmin)
