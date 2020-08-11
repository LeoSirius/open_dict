"""words_memo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from words_memo.views import home_view, profile_view, login_view, logout_view, \
    register_view
from words_memo.api.searh_words import SearchWordsView
from words_memo.api.user_words import UserWordsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('profile/', profile_view),

    path('accounts/login/', login_view, name='accounts-login'),
    path('accounts/logout/', logout_view, name='accounts-logout'),
    path('accounts/register/', register_view, name='accounts-register'),

    path('api/search-words/', SearchWordsView.as_view(), name='api-search-words'),

    path('api/user-words/', UserWordsView.as_view(), name='api-user-words'),


]
