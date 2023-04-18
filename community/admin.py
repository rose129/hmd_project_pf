from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('제목',{'fields':['title']}),
        ('내용',{'fields':['contents']}),
        ('작성자 정보',{'fields':["name", "email"]}),
        ('작성자 id', {'fields':['owner'],'classes':['collapse']}),
    ]
    list_display = ('pk','title','cdate')
    list_filter = ['cdate']
    search_fields = ['title','contents']

# Register your models here.
# admin.site.register(데이터모델, admin class) 전달인자 순서중요
admin.site.register(Article, ArticleAdmin)
