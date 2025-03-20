from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound, Http404

from .forms import AddPostForm
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
    if request.method == "POST":
        form=AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')

    else:
        form=AddPostForm()
    return render(request,'women/addpage.html',{'form':form,'title':'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
def show_post(request, post_slug):
    post=get_object_or_404(Women, slug=post_slug)
    context = {'post': post,
               'title': post.title,
               'cat_selected': post.cat_id,
               }
    return render(request,'women/post.html',context=context)
def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat=category)

    if not posts.exists():
        raise Http404()

    context = {'posts': posts,
               'title': 'Отображение по рубрикам',
               'cat_selected': category.slug,
               }
    return render(request, 'women/index.html', context=context)