from django.shortcuts import render, get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from blog.models import UserCommentDB, Content
from .serializers import CommentSerializer
from homepage.models import ShowcaseBlog
# Create your views here.

# class CommentList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'comment/comment_list.html'

#     def get(self, request):
#         user_comments = UserCommentDB.objects.all()
#         serializer = CommentSerializer(user_comments)
#         return Response({'serializer': serializer, 'comments': user_comments})

  
def CommentList(request, pk):
    # Querying the blog database
    blog_post = Content.objects.get(blog_category__id=pk)
    blog_lists = ShowcaseBlog.objects.all().order_by('id')
    comments = UserCommentDB.objects.filter(blog_title__id=pk).order_by('id')
    blog_title = UserCommentDB.objects.filter(blog_title__id=blog_post.id)
    
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
        # 'blog_post': blog_post,
        "blogs": blogs,
        "paginator": paginator,
        "comments": comments
    }
    return render(request, 'comment/comment_list.html', context)

def CommentEdit(request, pk):
    return HttpResponseRedirect(request.path_info) 


def CommentDelete(request, pk):
    # blog_post = Content.objects.get(blog_category__id=pk)
    blog_lists = ShowcaseBlog.objects.all().order_by('id')
    comments = UserCommentDB.objects.filter(blog_title__id=pk).order_by('id')
    # blog_title = UserCommentDB.objects.filter(blog_title__id=blog_post.id)

    comment = UserCommentDB.objects.get(id=pk)
       
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
        # 'blog_post': blog_post,
        "blogs": blogs,
        "paginator": paginator,
        "comments": comments
    }

    if comment:
        comment.delete()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'comment/comment_list.html', context)
 