from django.shortcuts import render
from django.core.paginator import Paginator
from .models import AboutHWC
from homepage.models import ShowcaseBlog
# Create your views here.

def about_blog(request):
    about_blog = AboutHWC.objects.get(go_online=True)
    blog_lists = ShowcaseBlog.objects.all().order_by('id')

    paginator = Paginator(blog_lists, 2)
    page_number =  request.GET.get('page', 1)
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
       "about": about_blog,
        "blogs": blogs,
        "paginator": paginator
    }
    return render(request, 'about_blog/haroffwebconsults.html', context)
