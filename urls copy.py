from django.contrib import admin
from django.urls import path, include

# 23.04.17 추가
from . import views

urlpatterns = [
    # 23.04.17 추가
    path('', views.index, name='index'),
    
    # 게시판 관리
    path('admin/', admin.site.urls),
    
    # 콘텐츠 - 대시보드
    path('dashboard_drug/', include('dashboard_drug.urls')),
]
