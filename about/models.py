from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class AboutDeveloper(models.Model):
    Title = models.CharField(max_length=100)
    about = RichTextField(blank=True, null=True)
    # About2 = RichTextField(blank=True, null=True)
    go_online = models.BooleanField(null=True)
    Profile_pic = models.ImageField(blank=True, null=True)
    Date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.Title