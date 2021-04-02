from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .models import SubscriberMail
from homepage.models import ShowcaseBlog
from django.contrib import messages

# Create your views here.
def register_mail(request):
    blog_listing = ShowcaseBlog.objects.filter(list=True).order_by('id')
    if request.method == 'POST':
        mail = request.POST['mail']
        if mail != '':
            sub_mail = SubscriberMail(email=mail)
            sub_mail.save()
            messages.add_message(request, messages.SUCCESS, 'You are succesfully subscribed to our newsletter! Navigate to home using above link.')
            return redirect('/register/mail')
        else:
            messages.add_message(request, messages.ERROR, 'Please provide your email to the newsletter form in the footer.')
    
    context = {
        "blog_listings": blog_listing
    }
    return render(request, 'register_mail/mail.html', context)
