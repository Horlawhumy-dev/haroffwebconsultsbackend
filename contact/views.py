from django.shortcuts import render
from django.core.mail  import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        subject = request.POST['subject']
        from_email = request.POST['email']
        message = request.POST['message']

        # # Send Mail
        # send_mail(
        #     fullname, # Fullname of messenger
        #     subject, # Subject or title of the message
        #     message, # Content of the message
        #     from_email, # email of the messenger, from
        #     ['haroffwebconsults@gmail.com',] # To mail
        # )

        # return render(request, 'contact/contact.html', {'fullname': fullname})

        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['haroffwebconsults@gmail.com', 'haroff.dev@gmail.com',], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'contact/contact.html', {'fullname': fullname})
        # else:
        #     # In reality we'd use a form class
        #     # to get proper validation errors.
        #     return HttpResponseRedirect('Make sure all fields are entered and valid.')
            
    return render(request, 'contact/contact.html')
