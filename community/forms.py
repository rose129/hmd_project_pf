from django.forms import ModelForm
from community.models import Article

class Form(ModelForm):
    class Meta:
        # 연결 model class 설정(데이터 테이블)
        model = Article
        fields = ["name", "title", "contents", "url", "email"]