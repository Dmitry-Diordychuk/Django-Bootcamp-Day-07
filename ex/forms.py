from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.forms.widgets import HiddenInput, TextInput, Textarea
from .models import Article, UserFavouriteArticle, User
from django.contrib.auth.forms import AuthenticationForm

class CreateArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'synopsis', 'content']
		widgets = {
			'title': TextInput(attrs={
				'class': "form-control",
			}),
			'synopsis': TextInput(attrs={
				'class': "form-control",
			}),
			'content': Textarea(attrs={
				'class': "form-control",
			})
		}
		labels = {
			'title': '',
			'synopsis': '',
			'content': '',
		}


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
		'class': 'form-control',
		'placeholder': "username",
		'aria-label': "username",
	}), label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder': "password",
		'aria-label': "password",
	}), label='')
