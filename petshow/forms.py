from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_title','article_text']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment_text', )

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма: ', max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email: ')
    # phone = forms.PhoneField(blank=True, help_text='Contact phone number')
    message = forms.CharField(label='Сообщение: ', widget=forms.Textarea)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
