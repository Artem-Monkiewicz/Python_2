"""hollymovies URL Configuration

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
from django.contrib import admin
from django.urls import path
from viewer.views import hello, rick_astley, hello_param,\
    hello_param_2, shorten_url, show_url, template_view,\
    movies_table, short_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('rick_astley/', rick_astley),
    path('hello_pram/<s>', hello_param),
    path('hello_param_2', hello_param_2),
    path('shorten_url', shorten_url),
    path('redirect/<shortcut>', show_url),
    path('tv', template_view),
    path('movies_table', movies_table),
    path('ShURL', short_url),
    path('movie_create_view', MovieCreateView.as_view(), name= 'movie_create' )
]

