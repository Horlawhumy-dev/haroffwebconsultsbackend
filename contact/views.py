from django.shortcuts import render, redirect
from django.core.mail  import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        subject = request.POST['subject']
        from_email = request.POST['email']
        body = request.POST['message']
        if fullname != '' and subject != '' and from_email != '' and body != '':
            msg_mail = str(body) + " " + str(from_email)
            #Send Mail
            try:
                send_mail(subject, msg_mail, from_email, ['haroffwebconsults@gmail.com'], fail_silently=False)
                messages.add_message(request, messages.SUCCESS, 'Success! Your message has been delivererd and will reply as soon as possible.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return render(request, 'contact/contact.html', {'fullname': fullname})
        else:
            messages.add_message(request, messages.ERROR, 'Please fill in all fields in the contact form!!')
        return redirect('/register/mail')
    return render(request, 'contact/contact.html')
