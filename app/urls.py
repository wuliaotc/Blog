"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views as app_views

urlpatterns = [
    path('',app_views.toIndex),
    path('register/', app_views.register),
    path('login/', app_views.login),
    path('logout/', app_views.logout),
    path('changePassword/', app_views.ChangePassword),
    path('userinfo/', app_views.showUserInfo),
    #path('is_login/', app_views.is_login), 废弃
    path('index/', app_views.index),
    path('articlelist/', app_views.GetArticleList),
    path('articleData/<int:article_id>', app_views.GetArticleData),
    path('article/<int:article_id>', app_views.ShowArticle),
    path('article/<int:article_id>/remove', app_views.delArticle),
    path('article/<int:article_id>/remark', app_views.addRemark),
    path('article/<int:article_id>/remark/<int:remark_id>',
         app_views.addReply),
    path('write/', app_views.writeblog)
]
