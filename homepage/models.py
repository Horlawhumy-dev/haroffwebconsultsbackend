from django.db import models

# Create your models here.
class ShowcaseBlog(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    new = models.BooleanField(null=True)
    list = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
