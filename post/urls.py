from django.urls import path
from post import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<post_id>', views.PostView.as_view()),
    path('upload/',views.PostView.as_view()),
    path('edit/<post_id>',views.PostView.as_view()),
    path('delete/<post_id>',views.PostView.as_view()),
    path('like/<post_id>',views.PostLikeView.as_view()),
    path('detail/',views.PostDetailView.as_view()),
    path('collection/', views.CollectionView.as_view()),
    path('purchase/<int:id>', views.purchase_art.as_view()),
]