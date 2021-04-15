from  django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('blog/<str:pk>/', views.CommentList, name='comment-list'),
    path('blog/<str:pk>/edits', views.CommentEdit, name='comment-edit'),
    path('blog/<str:pk>/delete', views.CommentDelete, name='comment-delete')
]
