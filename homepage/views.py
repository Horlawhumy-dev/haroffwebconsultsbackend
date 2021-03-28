from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import *

# Create your views here.

def index(request):
    blogs = ShowcaseBlog.objects.filter(new=True)
    blog_listing = ShowcaseBlog.objects.filter(list=True).order_by("-id")
    blog_lists = ShowcaseBlog.objects.all().order_by('-id')

    paginator = Paginator(blog_lists, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # about_content = AboutBlog.objects.get(go_online=True)
    context = {
        'blogs': blogs,
        "blog_listings": blog_listing,
        "page_obj": page_obj
    }
    return render(request, 'homepage/index.html', context)
