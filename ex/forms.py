from django import forms
from django.db.models import fields
from django.forms.widgets import HiddenInput
from .models import Article, UserFavouriteArticle, User

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
