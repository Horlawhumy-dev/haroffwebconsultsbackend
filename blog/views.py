from django.shortcuts import render, redirect

# from .models import Listing, BlogContent, BlogComment

# Create your views here.
def listing(request):
    # listings = Listing.objects.all()
    # context = { 
    #     "listings": listings
    #     }
    return render(request, 'blog/listings.html')

    
def blog_view(request):
    # Querying the blog database
    # blog_post = BlogContent.objects.all()
    return render(request, 'blog/blog.html', { 'blog_post': blog_post })


def comment_view(request):
    # comments = Comment.objects.all()
    if request.method == 'POST':
        name = request.POST['fullname']
        message = request.POST['message']
        if name and message:
            print(name, message)
            # comment = BlogComment(name=name, message=message)
            # comment.save()
            return redirect('/blog/main')
           
    # context = {'comments': comments}
    return render(request, 'blog/comment.html')