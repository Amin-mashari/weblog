from django.urls import path
from .views import home 
#ctrl + shift + i
app_name = 'blog'

urlpatterns = [
    path('', home, name='home')
]
