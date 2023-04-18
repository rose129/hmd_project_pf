from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article
# Create your views here.

# def Community(request):
#     return render( request, 'community/community.html')

class WriteFormView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["name", "title", "contents", "url", "email"]
    template_name = 'community/write.html'
    success_url = reverse_lazy('community:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ArticleLestView(ListView):
    model = Article
    template_name = 'community/list.html'

class ArticleViewDetail(DetailView):
    model = Article
    template_name = 'community/view_detail.html'