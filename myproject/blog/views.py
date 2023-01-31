from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse as HR
# from django.http import JsonResponse as JR
from .models import Article , Category

# Create your views here.


def home(request,page=1):

    article_list = Article.objects.published()
    paginator = Paginator(article_list , 1)
    articles = paginator.get_page(page)
    context = {
        'articles': articles,
    }
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/detail.html', context)


def category(request,slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True)
        
    }
    return render(request, 'blog/category.html', context)