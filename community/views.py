from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article
from .forms import Form
# Create your views here.

# def Community(request):
#     return render( request, 'community/community.html')

# 글작성
class WriteFormView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = Form
    # fields = ["name", "title", "contents", "email"]
    template_name = 'community/write.html'
    success_url = reverse_lazy('community:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# 게시글 리스트
class ArticleLestView(ListView):
    model = Article
    ordering = '-pk'
    # 한페이지당 보여줄 post 갯수 정하기
    paginate_by = 8
    template_name = 'community/list.html'

# 게시글
class ArticleViewDetail(DetailView):
    model = Article
    template_name = 'community/view_detail.html'

# 로그인된 작성자가 작성한글만 보이는 리스트
class ArticleChangeView(LoginRequiredMixin, ListView):
    # article write 시 owner 추가하기
    # 구현하고 다시 작성
    template_name = 'community/change_list.html'
    def get_queryset(self):
        return Article.objects.filter(owner= self.request.user)

# 게시글 수정
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ["name", "title", "contents", "email"]
    template_name = 'community/write_update.html'
    # community:list, id값 같이 넘기기 <= path name

    success_url = reverse_lazy('community:change_list')

# 게시글 삭제
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'community/write_delete.html'
    success_url = reverse_lazy('community:change_list')

