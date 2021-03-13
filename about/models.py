from django.db import models

# Create your models here.

class AboutDeveloper(models.Model):
    Title = models.CharField(max_length=100)
    About1 = models.TextField(blank=True, null=True)
    About2 = models.TextField(blank=True, null=True)
    go_online = models.BooleanField(null=True)
    Profile_pic = models.ImageField(blank=True, null=True)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Title