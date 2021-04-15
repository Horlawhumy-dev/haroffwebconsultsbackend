from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import SubscriberMail
from homepage.models import ShowcaseBlog
from django.contrib import messages

# Create your views here.
def register_mail(request):
    blog_listing = ShowcaseBlog.objects.filter(list=True).order_by('id')
    blog_lists = ShowcaseBlog.objects.all().order_by('id')
    paginator = Paginator(blog_lists, 2)
    page_number = request.GET.get('page', 1)

    if request.method == 'POST':
        mail = request.POST['mail']
        if mail != '':
            sub_mail = SubscriberMail(email=mail)
            sub_mail.save()
            messages.add_message(request, messages.SUCCESS, 'You are succesfully subscribed to our newsletter! Navigate to home using above link.')
            return redirect('/register/mail')
        else:
            messages.add_message(request, messages.ERROR, 'Please provide your email to the newsletter form in the footer.')
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blogs': blogs,
        # 'about_dev': about_dev,
        "blog_listings": blog_listing,
        "paginator": paginator
    }
    return render(request, 'register_mail/mail.html', context)
