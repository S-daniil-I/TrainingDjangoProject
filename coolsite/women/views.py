from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound, Http404
from .models import *
# Create your views here.

def index(request):
    posts=Women.objects.all()

    context={'posts':posts,
            'title':'Главная страница',
             'cat_selected':0,
             }
    return render(request,'women/index.html',context=context)
def about(request):
    return render(request, 'women/about.html', { 'title': 'О сайте'})
def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id {post_id}")
def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts)==0:
        raise Http404()

    context = {'posts': posts,
               'title': 'Отображение по рубрикам',
               'cat_selected': cat_id,
               }
    return render(request, 'women/index.html', context=context)