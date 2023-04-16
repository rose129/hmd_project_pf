from django.urls import path
from . import views

urlpatterns = [
    
  # /blog/ 
    path('', views.PostList.as_view(), name= "post_list"),
  # /blog/1/
    path('<int:pk>/', views.PostDetail.as_view(), name = "post_detail"), 

]