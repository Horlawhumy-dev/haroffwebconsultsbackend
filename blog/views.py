from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def listing(request):
    blog_listings = InfoBlog.objects.filter(new_post=True)
    context = { 
        "blog_listings": blog_listings
        }
    return render(request, 'blog/listings.html', context)

    
def blog_view(request, pk):
    # Querying the blog database
    blog_post = Content.objects.get(blog_category_id=pk)
    return render(request, 'blog/blog.html', { 'blog_post': blog_post })


def comment_view(request, pk):
    comments = Comment.objects.get(category_id=pk)
    # blog_post = Content.objects.get(blog_category_id=pk)
    if request.method == 'POST':
        name = request.POST['fullname']
        message = request.POST['message']
        if name and message:
            print(name, message)
            # comment = BlogComment(name=name, message=message)
            # comment.save()
            return redirect('/blog/main/blog.id')
           
    context = {'comments': comments}
    return render(request, 'blog/comment.html', context)