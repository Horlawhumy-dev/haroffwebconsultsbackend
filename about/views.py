from django.shortcuts import render
from django.core.paginator import Paginator

from homepage.models import ShowcaseBlog
from .models import AboutDeveloper

# Create your views here.

def about(request):
    about_dev = AboutDeveloper.objects.get(go_online=True)
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
    context = {
        'blogs': blogs,
        'about_dev': about_dev,
        "blog_listings": blog_listing,
        "paginator": paginator
    }
    return render(request, 'about/about.html', context)
