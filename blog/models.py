from django.db import models
from datetime import datetime

# Create your models here.

class InfoBlog(models.Model):
    blog = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=datetime, null=True)
    
    def __str__(self):
        return self.blog


class Content(models.Model):
    blog_category = models.ForeignKey('InfoBlog', null=True, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=100, null=True)
    content1 = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)
    content3 = models.TextField(blank=True, null=True)
    content4 = models.TextField(blank=True, null=True)
    content5 = models.TextField(blank=True, null=True)
    posted_by = models.CharField(max_length=100)
    content_pic = models.ImageField(blank=True, null=True)
    # online = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.blog_title


class UserCommentDB(models.Model):
    blog_title = models.ForeignKey('Content', null=True, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    date_commented = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user