from django.shortcuts import render
from django.http import HttpResponse

from .models import Stock
# Create your views here.


def hello(request):
    return HttpResponse("Hello, Let's start!")
