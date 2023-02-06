from django.core.paginator import Paginator
from django.views.generic import ListView
from account.models import User
from django.views.generic.detail import DetailView
from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse as HR
# from django.http import JsonResponse as JR
from .models import Article , Category
from account.mixins import AuthorAccessMixin

# Create your views here.


# def home(request,page=1):

#     article_list = Article.objects.published()
#     paginator = Paginator(article_list , 1)
#     articles = paginator.get_page(page)
#     context = {
#         'articles': articles,
#     }
#     return render(request, 'blog/home.html', context)

class ArticleList(ListView):
    # model = Article
    template_name = 'blog/article_list.html'

    queryset = Article.objects.published()
    paginate_by = 2



# def detail(request, slug):
#     context = {
#         'article': get_object_or_404(Article, slug=slug, status='p')
#     }
#     return render(request, 'blog/detail.html', context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return  get_object_or_404(Article.objects.published(), slug=slug)

class ArticlePreview(AuthorAccessMixin, DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return  get_object_or_404(Article, pk=pk)



# def category(request,slug,page=1):
    
#     category = get_object_or_404(Category, slug=slug, status=True)
#     article_list = category.articles.published()
#     paginator = Paginator(article_list , 1)
#     articles = paginator.get_page(page)
#     context = {
#         'category':category,
#         'articles':articles,
#     }
#     return render(request, 'blog/category.html', context)

class CategoryList(ListView):
    # model = Article
    # template_name = 'blog/home.html'

    paginate_by = 1
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return  category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    # model = Article
    # template_name = 'blog/home.html'

    paginate_by = 1
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return  author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context