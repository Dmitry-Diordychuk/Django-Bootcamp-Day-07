from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import HiddenInput
from .models import Article, UserFavouriteArticle, User
from django.contrib.auth.forms import AuthenticationForm

class CreateArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'synopsis', 'content']


class AddFavoriteForm(forms.ModelForm):
	class Meta:
		model = UserFavouriteArticle
		fields = ['article', 'user']
		widgets = {
            'article': HiddenInput(),
			'user': HiddenInput(),
        }


class PrettyAuthenticationForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control me-2',
		'placeholder': "username",
		'aria-label': "username",
	}), label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'class': 'form-control me-2',
		'placeholder': "password",
		'aria-label': "password",
	}), label='')
