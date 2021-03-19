from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import *

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
    comments = UserCommentDB.objects.filter(blog_title_id=pk)
    blog_title = UserCommentDB.objects.filter(blog_title_id=blog_post.id)
    
    if request.method == 'POST':
        name = request.POST['fullname']
        message = request.POST['message']
        if name and message:
            print(name, message)
            user_comment = UserCommentDB(blog_title=blog_post, user=name, message=message)
            user_comment.save()
            return HttpResponseRedirect(request.path_info)
    context = {
        'blog_post': blog_post,
        "comments": comments
    }
    return render(request, 'blog/blog.html', context)


# def comment_view(request, pk):
#     blog_post = Content.objects.get(blog_category_id=pk)
#     user_comment = UserComment.objects.get(header_id=pk)
#     # blog_post = Content.objects.get(blog_category_id=pk)
#     if request.method == 'POST':
#         name = request.POST['fullname']
#         message = request.POST['message']
#         if name and message:
#             # print(name, message)
#             user_comment = UserComment(category=blog_post, commentator_name=name, message=message)
#             user_comment.save()
#             return redirect(f"/blog/main/{blog_post.blog_category_id}")
           
#     context = {'user_comments': user_comment}
#     return render(request, 'blog/comment.html', context)