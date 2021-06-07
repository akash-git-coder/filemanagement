from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('welcome/<int:pk>/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
]