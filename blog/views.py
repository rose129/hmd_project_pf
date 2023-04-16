from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # 한페이지당 보여줄 post 갯수 정하기
    paginate_by = 3

    def get_context_data(self, **kwargs):

        context = super(PostList, self).get_context_data()

        return context

class PostDetail(DetailView):
    model = Post

   