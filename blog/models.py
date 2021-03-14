from django.db import models
from datetime import datetime

# Create your models here.

class InfoBlog(models.Model):
    blog = models.CharField(max_length=100)
    new_post = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now=datetime, null=True)
    
    def __str__(self):
        return self.blog


class Content(models.Model):
    title = models.ForeignKey('InfoBlog', on_delete=models.CASCADE)
    content1 = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)
    content3 = models.TextField(blank=True, null=True)
    content4 = models.TextField(blank=True, null=True)
    content5 = models.TextField(blank=True, null=True)
    posted_by = models.CharField(max_length=100)
    content_pic = models.ImageField(blank=True, null=True)
    online = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_title = models.ForeignKey('Content', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name