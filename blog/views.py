from django.shortcuts import render



# Create your views here.
def listing(request):
    # listing = Listing.objects.all()
    # context = { 
    #     "listings": listing
    #     }
    return render(request, 'blog/listings.html')

    
def blog_view(request, pk):
    # Querying the blog database
    # blog_post = Blog.objects.get(id=pk, go_online=True)
    return render(request, 'blog/blog.html', { 'blog_post': blog_post })


def comment_view(request):
    # comments = Comment.objects.all()
    # if request.method == 'POST':
    #     name = request.POST['fullname']
    #     message = request.POST['message']
        # if name and message:
            # print(name, message)
            # comment = Comment(fullname=name, message=message)
            # comment.save()
    # context = {'comments': comments}
    return render(request, 'blog/comment.html')