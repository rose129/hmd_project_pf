from django.shortcuts import render

# Create your views here.


def Portfolio(request):
    return render( request, 'portfolio/portfolio.html')

# 토이프로젝트
def WordgameLanding(request):
    return render( request, 'portfolio/start.html')
def Wordgame(request):
    return render( request, 'portfolio/wordgame.html')
