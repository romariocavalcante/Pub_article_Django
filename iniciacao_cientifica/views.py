from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def login(request):
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request, 'registration/login.html', context)


def home(request):
    article = Article.objects.all()
    user = User.objects.all()
    context = {
        'article': article,
        'user': user,
        }
        
    return render(request, 'home.html', context)

def profile(request):
    
    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():
            salvar = form.save(commit=False)
            salvar.done = 'doing'
            salvar.save()
            return redirect('/user')
    else:
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'profile.html', context)
  

def article(request):

    if request.method == 'POST':

        form = ArticleForm(request.POST)

        if form.is_valid():
            salvar = form.save(commit=False)
            salvar.done = 'doing'
            salvar.save()
            return redirect('/')
    else:
        form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, 'article.html', context)


def user(request):
    user = User.objects.all()
    context = {
        'user': user,
        }
        
    return render(request, 'user.html', context)


def deleteUser(request, id):
    user = User.objects.all()
    dlt = User.objects.get(id=id)
    if request.method == 'POST':
        dlt.delete()        
        return redirect('user')
        
    else:
        context = {
            'user':user,
            'dlt':dlt,
        }
        return render(request, 'deleteUser.html', context)

    

