from django.contrib import admin
from .models import InfoBlog, Content, Comment


# Register your models here.
admin.site.register(InfoBlog)
admin.site.register(Content)
admin.site.register(Comment)

