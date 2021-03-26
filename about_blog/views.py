from django.shortcuts import render

# Create your views here.

def about_blog(request):
    return render(request, 'about_blog/haroffwebconsults.html')
