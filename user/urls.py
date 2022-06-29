from django.contrib import admin
from django.urls import path, include
from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # 기본 JWT access토큰 발급 view
    TokenRefreshView) # JWT Refresh 토큰 발급 view

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('model/', views.ModelView.as_view(), name='deep_learning'),
]
