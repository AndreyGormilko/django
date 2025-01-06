from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def articles(request, articles_id):
    article = Articles.objects.get(id=articles_id)
    context = {'article': article}
    return render(request, 'news/details_view.html', context)

@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('news:news_home')
        else:
            error = 'Form is not valid'
    form = ArticlesForm()
    context = {'form': form, 'error': error,}
    return render(request, 'news/create.html', context)

@login_required
def edit(request, articles_id):
    articles = Articles.objects.get(id=articles_id)
    check_user(request, articles)
    if request.method != 'POST':
        form = ArticlesForm(instance=articles)
    else:
        form = ArticlesForm(instance=articles, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:news_home')
    context = {'articles': articles, 'form': form}
    return render(request, 'news/create.html', context)

@login_required
def delete(request, articles_id):
    articles = Articles.objects.get(id=articles_id)
    check_user(request, articles)
    if request.method != 'POST':
        pass
    else:
        articles.delete()
        return redirect('news:news_home')
    context = {'articles': articles}
    return render(request, 'news/delete.html', context)

def check_user(request, articles):
    if articles.owner != request.user:
        raise Http404("This post is not your")
