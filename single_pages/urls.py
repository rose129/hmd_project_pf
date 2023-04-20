from django.urls import path
from . import views

urlpatterns = [
    # main
    path('', views.Landing),
    # about me
    path('about_me/', views.AboutMe),
    
]


