from django.contrib import admin
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:articles_id>', views.articles, name='news_detail'),
    path('<int:articles_id>/update', views.edit, name='news_update'),
    path('<int:articles_id>/delete', views.delete, name='news_delete'),
]
