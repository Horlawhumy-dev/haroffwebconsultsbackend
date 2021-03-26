from django.db import models
from django.utils import timezone

# Create your models here.
class AboutHWC(models.Model):
    headlines = models.CharField(max_length=100, null=True)
    about_blog1 = models.TextField(null=True)
    about_blog2 = models.TextField(null=True)
    about_blog2 = models.TextField(null=True)
    go_online = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.headlines
