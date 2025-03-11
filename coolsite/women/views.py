from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound, Http404
# Create your views here.
def index(request):
    return HttpResponse('Page of app women.')
def categories(request,cat):
    print(request.POST)
    return HttpResponse(f'<h1>Categories</h1>{cat}</p>')
def archive(request,year):
    if int(year)>2020:
        return redirect('home',permanent=True)
    return HttpResponse(f'<h1>Archive by years</h1>{year}</p>')
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')