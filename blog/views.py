from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

from django.shortcuts import get_object_or_404
from .models import Post, Category, Tag, Comment
from .forms import PostForm
from .forms import CommentForm


# Create your views here.

# Post list 
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # 한페이지당 보여줄 post 갯수 정하기
    paginate_by = 3

    def get_context_data(self, **kwargs):

        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        # Post 테이블에서 category 필드를 선택안 한 포스트의 갯수
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context
# post detail
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        # Post 테이블에서 category 필드를 선택안 한 포스트의 갯수
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm

        return context
    

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    # 템플릿 네임이 post_form이 아닐경우 꼭 써줘야 한다
    # template_name = 'blog/post_form.html'
    # fields = ['title','hook_text','content','head_image','file_upload','category']

    # 최고 관리자와 스태프만 글을 작성하게한다
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
        

    def form_valid(self, form):
        current_user = self.request.user

        # 최고 관리자와 스태프만 글을 작성하게한다
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            
            # tag_str로 받은 값의 쉼표 ','를 세미콜론 ';'으로 모두 변경한 후 세미콜론으로 split해서 리스트 형태로 tags_list에 담고
            # strip()으로 앞뒤의 공백을 제거 후 같은 name을 갖는 태그가 있다면 가져오고, 없다면 새로 만듬 중복x
           
            response = super(PostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')

            if tags_str:

                tags_str = tags_str.strip()

                tags_str = tags_str.replace(',', ';')
                tags_list = tags_str.split(';')
                # print(tags_list)

                for t in tags_list:
                    # print(t)
                    t = t.strip()
                    if t == '':
                        continue
                    else:
                        # 예외상황 공백이 아닌거
                        tag, is_tag_created = Tag.objects.get_or_create(name=t)
                        # tag 공백일 때는 pass
                        if is_tag_created:
                            tag.slug = slugify(t, allow_unicode=True)
                            tag.save()

                        self.object.tags.add(tag)

            return response

        else:
            return redirect('/blog/')
        
# PostUpdate() 클래스로 CBV형식의 view 작성 
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    # Update Form을 django 라이브러리인 summernote로 구현
    form_class = PostForm

    template_name = 'blog/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] ='; '.join(tags_str_list)
        return context
    
        
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied  

    def form_valid(self, form):
            
            response = super(PostUpdate, self).form_valid(form)
            self.object.tags.clear()

            tags_str = self.request.POST.get('tags_str')

            if tags_str:
                tags_str = tags_str.strip()
                tags_str = tags_str.replace(',', ';')
                tags_list = tags_str.split(';')
        
                for t in tags_list:
                    # print(t)
                    t = t.strip()
                    if t == '':
                        continue
                    else:
                        # 예외상황 공백이 아닌거
                        tag, is_tag_created = Tag.objects.get_or_create(name=t)
                        # tag 공백일 때는 pass
                        if is_tag_created:
                            tag.slug = slugify(t, allow_unicode=True)
                            tag.save()

                        self.object.tags.add(tag)

            return response


def category_page(request, slug):
    
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
        
    # 선택한 슬러그의 해당하는 category테이블의 레코드
    context = {
        'post_list' : post_list,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        'category': category,
    }
    return render(request, 'blog/post_list.html',context)

def tag_page(request, slug):
    
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        'post_list' : post_list,
        'tag' : tag,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
    }

    return render(request, 'blog/post_list.html',context)

class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q) | Q(content__contains=q)
        ).distinct()
        return post_list
    
    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'
        
        return context

# 댓글달기
def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
# 댓글수정
class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

# 댓글 삭제
def delete_comment(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post

    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        
        raise PermissionDenied