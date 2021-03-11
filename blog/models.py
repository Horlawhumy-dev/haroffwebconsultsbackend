from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog1 = models.TextField(blank=True, null=True)
    blog2 = models.TextField(blank=True, null=True)
    blog3 = models.TextField(blank=True, null=True)
    blog4 = models.TextField(blank=True, null=True)
    blog5 = models.TextField(blank=True, null=True)
    posted_by = models.CharField(max_length=100)
    blog_pic = models.ImageField(blank=True, null=True)
    go_online = models.BooleanField(null=True)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fullname