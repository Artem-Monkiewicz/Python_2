import random
import string

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import ShortUrls


# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World!<h1>")

def rick_astley(request):
    response = redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    return response

def hello_param(request, s):
    return HttpResponse(f'Hello {s}')

def hello_param_2(request):
    name = request.GET.get('name', '')
    return HttpResponse(f'Hello {name}')

def shorten_url(request):
    url_to_shorten = request.GET.get('url', '')
    if url_to_shorten:
        short_url = ''.join([random.choice(string.ascii_letters + '123456789') for _ in range(5)])
        ShortUrls.objects.create(url=url_to_shorten, short_url=short_url)
        return HttpResponse(f'OK! url is: {short_url}')
    else:
        return HttpResponse('Please enter a valid URL')

def show_url(request, shortcut):
    if shortcut:
        url=ShortUrls.objects.get(short_url=shortcut)
        return redirect(url_record.url)
    else:
        return HttpResponse("No shortcut provided!")