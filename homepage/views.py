from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
# def base(request):
#     return render(request, 'homepage/base.html', {})


def index(request):
    blogs = ShowcaseBlog.objects.filter(new=True)
    blog_listing = ShowcaseBlog.objects.filter(list=True)
    context = {
        'blogs': blogs,
        "blog_listings": blog_listing
    }
    return render(request, 'homepage/index.html', context)
