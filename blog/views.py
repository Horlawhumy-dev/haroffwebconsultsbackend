from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import *
from homepage.models import ShowcaseBlog
# Create your views here.
def listing(request):
    blog_listings = ShowcaseBlog.objects.filter(list=True).order_by('id')
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
        "blogs": blogs,
        "paginator": paginator
        }
    return render(request, 'blog/listings.html', context)

    
def blog_view(request, pk):
    # Querying the blog database
    blog_post = Content.objects.get(blog_category_id=pk)
    blog_lists = ShowcaseBlog.objects.all().order_by('id')
    comments = UserCommentDB.objects.filter(blog_title_id=pk).order_by('id')
    blog_title = UserCommentDB.objects.filter(blog_title_id=blog_post.id)
    
    if request.method == 'POST':
        name = request.POST['fullname']
        message = request.POST['message']
        if name != '' and message != '':
            user_comment = UserCommentDB(blog_title=blog_post, user=name, message=message)
            user_comment.save()
        else:
            return HttpResponseRedirect(request.path_info)
    # Django pagination
    paginator = Paginator(blog_lists, 2)
    page_number =  request.GET.get('page', 1)
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blog_post': blog_post,
        "blogs": blogs,
        "paginator": paginator,
        "comments": comments
    }
    return render(request, 'blog/blog.html', context)
