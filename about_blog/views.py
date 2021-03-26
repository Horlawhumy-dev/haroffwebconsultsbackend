from django.shortcuts import render
from .models import AboutHWC
from homepage.models import ShowcaseBlog
# Create your views here.

def about_blog(request):
    about_blog = AboutHWC.objects.get(go_online=True)
    blog_listing = ShowcaseBlog.objects.filter(list=True)
    context = {
       "about": about_blog,
        "blog_listings": blog_listing
    }
    return render(request, 'about_blog/haroffwebconsults.html', context)
