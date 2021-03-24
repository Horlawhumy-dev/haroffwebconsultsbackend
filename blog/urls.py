
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.listing, name="index"),
    path('main/<str:pk>/', views.blog_view, name="main"),
    path('delete_comment/<str:pk>/', views.deleteComment, name="delete_comment"),
    path('update_comment/<str:pk>/', views.updateComment, name="update_comment")
]
