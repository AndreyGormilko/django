from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomLoginView

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
]
