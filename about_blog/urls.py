
from django.urls import path

from . import views

app_name = 'about_blog'
urlpatterns = [
    path('H-W-C/', views.about_blog, name="index")
] 
