from django.contrib import admin
from .models import Listing, BlogContent, BlogComment


# Register your models here.
admin.site.register(Listing)
admin.site.register(BlogContent)
admin.site.register(BlogComment)

