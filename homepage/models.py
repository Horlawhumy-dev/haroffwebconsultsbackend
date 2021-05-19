from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class ShowcaseBlog(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = RichTextField(null=True)
    new = models.BooleanField(null=True)
    list = models.BooleanField(null=True)
    author = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.title



