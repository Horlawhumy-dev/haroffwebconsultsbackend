from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import random,string
# Create your models here.

class InfoBlog(models.Model):
    blog = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    author = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.blog

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Content(models.Model):
    blog_category = models.ForeignKey('InfoBlog', null=True, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=100, null=True)
    content = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=100, null=True)
    content_pic = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    slug = models.SlugField(max_length=200)
    
    def save(self):
        if not self.slug:
            self.slug = slugify(rand_slug() + "_" + self.blog_title.lower(), allow_unicode=True)
        super(Content, self).save()
    
    def __str__(self):
        return self.blog_title


class UserCommentDB(models.Model):
    blog_title = models.ForeignKey('Content', null=True, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    date_commented = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.user