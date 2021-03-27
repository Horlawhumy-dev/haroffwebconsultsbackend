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
            #Send Mail
            try:
                send_mail(subject, body, from_email, ['haroffwebconsults@gmail.com', 'haroff.dev@gmail.com',], fail_silently=False)
                messages.add_message(request, messages.SUCCESS, 'Success! Your message has been delivererd and will reply as soon as possible.')
                return redirect('/register/mail')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'contact/contact.html', {'fullname': fullname})
        else:
            messages.add_message(request, messages.ERROR, 'Please fill in all fields!!')

    return render(request, 'contact/contact.html')
