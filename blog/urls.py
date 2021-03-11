
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.blog_view, name="blog"),
    path('comment/', views.comment_view, name="comment")
]
