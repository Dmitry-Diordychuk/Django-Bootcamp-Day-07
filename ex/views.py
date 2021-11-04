from django.contrib.auth import views
from django.db import models
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from .models import Article, UserFavouriteArticle
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import CreateArticleForm, AddFavoriteForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.forms import AuthenticationForm
from .forms import PrettyAuthenticationForm

# Create your views here.
class Home(RedirectView):
	url = 'articles'


class Articles(ListView):
	model = Article
	extra_context = {
		"login_form": PrettyAuthenticationForm(),
		"current_page": "articles",
	}


class Login(LoginView):
	extra_context = {"login_form": PrettyAuthenticationForm()}

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().post(request, *args, **kwargs)



class Publications(ListView):
	model = Article
	template_name = 'ex/publication_list.html'
	extra_context = {
		"current_page": "publications",
	}

	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().get(request, *args, **kwargs)


class ArticleDetail(DetailView, FormMixin):
	model = Article
	template = 'ex/article.html'
	context_object_name = 'article'
	form_class = AddFavoriteForm
	initial = {}
	extra_context = {"login_form": PrettyAuthenticationForm()}

	def setup(self, request, *args, **kwargs) -> None:
		self.initial["user"] = request.user.id
		self.initial["article"] = kwargs.get('pk')
		return super().setup(request, *args, **kwargs)


@login_required
class Logout(LogoutView):
	pass


class Favourites(ListView):
	model = Article
	template_name = 'ex/favourite_list.html'
	extra_context = {
		"current_page": "favourites",
	}

	def get_queryset(self):
		articles = (
			UserFavouriteArticle
			.objects
			.filter(user=self.request.user)
		)
		return articles

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().get(request, *args, **kwargs)


class Register(SuccessMessageMixin, CreateView):
	success_url = reverse_lazy('login')
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	extra_context = {
		"login_form": PrettyAuthenticationForm(),
		"current_page": "register",
	}

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().post(request, *args, **kwargs)


class ArticleCreate(CreateView):
	model = Article
	form_class = CreateArticleForm
	success_url = reverse_lazy('publications')
	template_name = "ex/article_create.html"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect(reverse_lazy('home'))
		return super().post(request, *args, **kwargs)


class AddFavorite(CreateView):
	model = UserFavouriteArticle
	form_class = AddFavoriteForm
	template_name = "ex/favourite_list.html"
	success_url = reverse_lazy("favourites")

	def form_invalid(self, form):
		return redirect(reverse_lazy('favourites'))

	def get(self, request, *args, **kwargs):
		return redirect(reverse_lazy('home'))

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect(reverse_lazy('home'))


		return super().post(request, *args, **kwargs)
