from django.shortcuts import render
from .models import AboutDeveloper

# Create your views here.

def about(request):
    about_dev = AboutDeveloper.objects.get(id=1)

    return render(request, 'about/about.html', {'about_dev': about_dev})
