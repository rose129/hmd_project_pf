from django import forms
from .models import Post
from .models import Comment

from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','head_image','file_upload','category','tags']
        widgets = {
            'content': SummernoteWidget(attrs={
            'toolbar': [
                    ['fontname', ['fontname']],
                    ['fontsize', ['fontsize']],
                    ['style', ['bold', 'italic', 'underline','strikethrough', 'clear']],
                    ['color', ['forecolor','color']],
                    ['table', ['table']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['height', ['height']],
                    ['insert',['picture','link','video']],
                    ['view', ['fullscreen', 'help']]
                ],
                'fontNames': ['Arial', 'Arial Black', 'Comic Sans MS', 'Courier New','맑은 고딕','궁서','굴림체','굴림','돋움체','바탕체'],
                'fontSizes': ['8','9','10','11','12','14','16','18','20','22','24','28','30','36','50','72']
	  }
            
            ),
        }
# comment form 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)