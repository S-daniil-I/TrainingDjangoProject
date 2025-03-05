from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Page of app women.')
def categories(request):
    return HttpResponse('<h1>Categories</h1>')