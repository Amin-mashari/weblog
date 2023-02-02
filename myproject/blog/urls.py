from django.urls import path
from .views import ArticleList, detail ,category
#ctrl + shift + i
app_name = 'blog'

urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('article/<slug:slug>', detail, name='detail'),
    path('category/<slug:slug>', category, name='category'),
    path('category/<slug:slug>/page/<int:page>',category, name='category')
]
