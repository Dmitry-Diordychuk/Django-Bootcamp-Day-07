from django.contrib import admin
from django.urls import path
from django.urls.exceptions import NoReverseMatch
from .views import \
    Articles, \
    Favourites, \
    Home, \
    Login, \
    Publications, \
    ArticleDetail, \
    LogoutView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('articles/', Articles.as_view(), name='articles'),
    path('login/', Login.as_view(), name='login'),
    path('publications/', Publications.as_view(), name='publications'),
    path('detail/<str:pk>', ArticleDetail.as_view(), name='detail'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('favourites/', Favourites.as_view(), name="favourites"),
]
