from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Portfolio),
    path('start/', views.WordgameLanding),
    path('wordgame/', views.Wordgame),
]


