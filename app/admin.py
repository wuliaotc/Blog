from django.contrib import admin
from .models import User,Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=['Title','Author','Launch_Time','Edit_Time']


admin.site.register(User)
admin.site.register(Article,ArticleAdmin)