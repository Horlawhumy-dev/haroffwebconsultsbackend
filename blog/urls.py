
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.listing, name="index"),
    path('main/', views.blog_view, name="main"),
    path('comment/', views.comment_view, name="comment")
]
