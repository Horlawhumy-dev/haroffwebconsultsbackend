
from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
    path('dev/', views.about, name="index")
] 
