from django.urls import path
from . import views
from .views import register_view
from .views import login_view  # views.py'den login_view fonksiyonunu import ediyoruz
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('create-post/', views.create_post, name='create_post'),
    path('profile/', views.profile_view, name='profile'),  # Yeni eklenen satır

]