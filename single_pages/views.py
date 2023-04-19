from django.shortcuts import render

# Create your views here.

def Landing(request):
    return render( request, 'single_pages/main.html')

def AboutMe(request):
    return render( request, 'single_pages/about_me.html')


