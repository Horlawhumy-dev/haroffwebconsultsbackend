
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', include('about.urls')),
    path('', include('blog.urls')),
    path('', include('contact.urls')),
]
