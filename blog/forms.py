from django import forms
from .models import Post
from .models import Comment

from django_summernote.widgets import SummernoteWidget

# comment form 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','head_image','file_upload','category','tags']
        widgets = {
            'content': SummernoteWidget() }