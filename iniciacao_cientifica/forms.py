from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



