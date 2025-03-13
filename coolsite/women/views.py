from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound, Http404
from .models import *
# Create your views here.

menu=["About site","Add article","Feedback","Login"]
def index(request):
    posts=Women.objects.all()
    return render(request,'women/index.html',{'posts':posts,'menu':menu,'title':'Main page'})
def about(request):
    return render(request,'women/about.html',{'menu':menu,'title':'About site'})
def categories(request,cat):
    print(request.POST)
    return HttpResponse(f'<h1>Categories</h1>{cat}</p>')
def archive(request,year):
    if int(year)>2020:
        return redirect('home',permanent=True)
    return HttpResponse(f'<h1>Archive by years</h1>{year}</p>')
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')