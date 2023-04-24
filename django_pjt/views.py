from allauth.account.views import PasswordChangeView
from django.urls import reverse
from single_pages.views import Landing
from django.shortcuts import redirect




class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')