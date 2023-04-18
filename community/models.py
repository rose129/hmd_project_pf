from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    name = models.CharField( max_length = 20 )
    title = models.CharField( max_length = 50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField( auto_now_add = True )
    mdate = models.DateTimeField( auto_now = True )

    # on_delete= models.CASCADE : 계정이 삭제 되면 그 계정이 삭제한 글도 삭제함
    # blank=True : 입력폼에서 비어있는 것 허용
    # null=True : 테이블의 owner 컬럼에 빈값을 허용
    owner = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name_plural = "자유게시판"
        ordering = ('-mdate',) # mdate 기준 내림차순 정렬

# 문자열 format : title, name, cdate
    def __str__(self):
        return f'{self.title} : {self.name} : {self.cdate}'
    
    def get_absolute_url(self):
        # 'community:view_detail' : path 이름
        return reverse('community:view_detail', args=(self.id,))
    
   