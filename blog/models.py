from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class InfoBlog(models.Model):
    blog = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    author = models.CharField(max_length=100, null=True)

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
    author = models.CharField(max_length=100, null=True)
    content_pic = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.blog_title


class UserCommentDB(models.Model):
    blog_title = models.ForeignKey('Content', null=True, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    date_commented = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.user