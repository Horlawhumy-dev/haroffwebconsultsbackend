from django.shortcuts import render

from .models import Blog, Comment

# Create your views here.

def blog_view(request):
    blog_post = Blog.objects.get(go_online=True)
    return render(request, 'blog/blog.html', { 'blog_post': blog_post})


def comment_view(request):
    # comments = Comment.objects.all()
    if request.method == 'POST':
        name = request.POST['fullname']
        message = request.POST['message']
        if name and message:
            # print(name, message)
            # comment = Comment(fullname=name, message=message)
            # comment.save()
    # context = {'comments': comments}
    return render(request, 'blog/comment.html')