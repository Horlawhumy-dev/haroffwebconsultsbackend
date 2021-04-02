from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import *
from about_blog.models import AboutHWC

# Create your views here.

def index(request):
    about_HWC = AboutHWC.objects.get(go_online=True)
    blog_listing = ShowcaseBlog.objects.filter(list=True).order_by('id')
    blog_lists = ShowcaseBlog.objects.all().order_by('id')

    paginator = Paginator(blog_lists, 2)
    page_number = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    # about_content = AboutBlog.objects.get(go_online=True)
    context = {
        'blogs': blogs,
        "blog_listings": blog_listing,
        "about_hwc": about_HWC,
        "paginator": paginator
    }
    return render(request, 'homepage/index.html', context)
