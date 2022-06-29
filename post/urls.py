from django.urls import path
from post import views

urlpatterns = [
    path('<post_id>', views.PostView.as_view()),
    path('upload/',views.PostView.as_view()),
    path('edit/<post_id>',views.PostView.as_view()),
    path('delete/<post_id>',views.PostView.as_view()),
    
]