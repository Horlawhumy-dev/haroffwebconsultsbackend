from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .models import SubscriberMail
from django.contrib import messages

# Create your views here.
def register_mail(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        if mail != '':
            sub_mail = SubscriberMail(email=mail)
            sub_mail.save()
            messages.add_message(request, messages.SUCCESS, 'You are succesfully subscribed to our newsletter! Navigate to home using above link.')
            return redirect('/register/mail')
        else:
            messages.add_message(request, messages.ERROR, 'Please add your mail in the form.')
    return render(request, 'register_mail/mail.html')
