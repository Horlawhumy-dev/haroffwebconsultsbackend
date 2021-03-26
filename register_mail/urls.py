from django.urls import path
from . import views

app_name = 'register_mail'
urlpatterns = [
    path('mail/', views.register_mail, name='register')
]
