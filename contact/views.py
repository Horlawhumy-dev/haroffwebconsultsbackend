from django.shortcuts import render
from django.core.mail  import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        # Send Mail
        send_mail(
            fullname, # Fullname of messenger
            subject, # Subject or title of the message 
            email, # email of the messenger, from
            ['harof.dev@gmail.comm',] # To mail
        )

        context = {'fullname': fullname}
    return render(request, 'contact/contact.html', context)
