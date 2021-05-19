from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class AboutHWC(models.Model):
    headlines = models.CharField(max_length=100, null=True)
    about_blog = RichTextField(null=True)
    go_online = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.headlines
