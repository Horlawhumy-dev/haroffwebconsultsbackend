from django.shortcuts import render
from django.core.mail  import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

# Create your views here.

def contact(request):
    # message = messages()
    if request.method == 'POST':
        fullname = request.POST['fullname']
        subject = request.POST['subject']
        from_email = request.POST['email']
        body = request.POST['message']
        if fullname != '' and subject != '' and from_email != '' and body != '':
        # # Send Mail
        # send_mail(
        #     fullname, # Fullname of messenger
        #     subject, # Subject or title of the message
        #     message, # Content of the message
        #     from_email, # email of the messenger, from
        #     ['haroffwebconsults@gmail.com',] # To mail
        # )

        # return render(request, 'contact/contact.html', {'fullname': fullname})

        # if subject and body and from_email:
            message = messages.success(request, 'Your message is sent successfully!')
            try:
                send_mail(subject, body, from_email, ['haroffwebconsults@gmail.com', 'haroff.dev@gmail.com',], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'contact/contact.html', {'fullname': fullname})
        else:
            message = messages.error(request, 'Please fill in all fields!')
        #     # In reality we'd use a form class
        #     # to get proper validation errors.
        #     return HttpResponseRedirect('Make sure all fields are entered and valid.')
    # context = {
    #     "messages": message,
    #     "fullname": fullname
    # }
    return render(request, 'contact/contact.html')
