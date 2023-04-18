from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    # list
    path('', views.ArticleLestView.as_view(), name="list"),
    # write
    path('write/', views.WriteFormView.as_view(), name="write"),
    # view_detail
    path('view_detail/<int:pk>/', views.ArticleViewDetail.as_view(), name="view_detail"),
]
