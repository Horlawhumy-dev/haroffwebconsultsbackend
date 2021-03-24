from django.shortcuts import render

from homepage.models import ShowcaseBlog
from .models import AboutDeveloper

# Create your views here.

def about(request):
    about_dev = AboutDeveloper.objects.get(go_online=True)
    blog_listing = ShowcaseBlog.objects.filter(list=True)
    context = {
        'about_dev': about_dev,
        "blog_listings": blog_listing
    }
    return render(request, 'about/about.html', context)
