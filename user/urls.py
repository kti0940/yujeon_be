from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
    path('', views.UserView.as_view()),
]
