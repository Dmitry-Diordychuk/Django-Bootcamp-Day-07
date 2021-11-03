from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Article
from django.contrib import auth

# Create your views here.
class Home(RedirectView):
	url = 'articles'


class Articles(ListView):
	model = Article


class Login(LoginView):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			auth.logout(request)
			return redirect(reverse_lazy('home'))
		return super().get(request, *args, **kwargs)
