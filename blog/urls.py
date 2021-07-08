
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('list/', views.listing, name="index"),
    path('main/<slug:slug>/', views.blog_view, name="main")
]
