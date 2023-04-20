from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Category(models.Model):
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def  __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'
        
    class Meta:
        verbose_name_plural = 'Categories'



class Post(models.Model):
    
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_post')
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    
    def get_file_name(self):
        f_name = os.path.basename(self.file_upload.name)
        # print(f_name)
        return f_name
    
    def get_file_ext(self):
        f_ext = self.get_file_name().split('.')[-1]
        return f_ext
    
# Comment모델 추가
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'
    
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
    
    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/1498/dbbb6c39f5c801fd/svg/{self.author.email}'
