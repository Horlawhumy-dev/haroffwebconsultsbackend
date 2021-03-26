from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .models import SubscriberMail

# Create your views here.
def register_mail(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        if mail:
            print(mail)
            # sub_mail = SubscriberMail(email=mail)
            # sub_mail.save()
            # return redirect('/register/mail')
    return render(request, 'register_mail/mail.html')
