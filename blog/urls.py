from django.urls import path
from . import views

urlpatterns = [
    
  # /blog/ 
    path('', views.PostList.as_view(), name= "post_list"),
  # /blog/1/
    path('<int:pk>/', views.PostDetail.as_view(), name = "post_detail"), 
  # /blog/category/카테고리
    path( 'category/<str:slug>/', views.category_page, name = "category_filter"),
  # 글쓰기
    path('create_post', views.PostCreate.as_view()),
  # 작성한 글을 수정하기 위한 url path를 정의
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
  # 태그
    path('tag/<str:slug>/', views.tag_page),
  

]