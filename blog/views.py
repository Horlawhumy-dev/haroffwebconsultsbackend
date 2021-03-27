from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import *
from django.contrib import messages

# Create your views here.
def listing(request):
    blog_listings = InfoBlog.objects.all().order_by('-id')
    context = { 
        "blog_listings": blog_listings
        }
    return render(request, 'blog/listings.html', context)

    
def blog_view(request, pk):
    # Querying the blog database
    blog_post = Content.objects.get(blog_category_id=pk)
    comments = UserCommentDB.objects.filter(blog_title_id=pk).order_by('-id')
    blog_title = UserCommentDB.objects.filter(blog_title_id=blog_post.id)
    
    if request.method == 'POST':
        name = request.POST['fullname']
        message = request.POST['message']
        if name != '' and message != '':
            # print(name, message)
            user_comment = UserCommentDB(blog_title=blog_post, user=name, message=message)
            user_comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comments got posted successfully!!')
        else:
            messages.add_message(request, messages.ERROR, 'Kindly fill in all fields!!')
            return HttpResponseRedirect(request.path_info)
    context = {
        'blog_post': blog_post,
        "comments": comments
    }
    return render(request, 'blog/blog.html', context)

def updateComment(request, pk):
    comment = UserCommentDB.objects.get(blog_title_id=pk)
    user_comment = UserCommentDB(instance=comment)
    if request.method == 'POST':
        user_comment = UserCommentDB(request.POST, instance=comment)
        user_comment.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'blog/blog.html')


def deleteComment(request, pk):
    blog_post = Content.objects.get(blog_category_id=pk)
    comment = UserCommentDB.objects.filter(blog_title_id=pk)
    if comment:
        comment.delete()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'blog/blog.html')

    
