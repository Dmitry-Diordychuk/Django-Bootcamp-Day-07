from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Article, UserFavouriteArticle
from django.contrib import auth

# Create your views here.
class Home(RedirectView):
	url = 'articles'


class Articles(ListView):
	model = Article


class Login(LoginView):
	pass


class Publications(ListView):
	model = Article
	template_name = 'ex/publication_list.html'

	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)


class ArticleDetail(DetailView):
	model = Article
	template = 'ex/article.html'
	context_object_name = 'article'


class Logout(LogoutView):
	pass


class Favourites(ListView):
	model = Article
	template_name = 'ex/favourite_list.html'

	def get_queryset(self):
		return (
			UserFavouriteArticle
				.objects
				.filter(user=self.request.user)
				.select_related('article')
		)
