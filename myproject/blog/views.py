from django.shortcuts import render
from django.http import HttpResponse as HR
from django.http import JsonResponse as JR

# Create your views here.


def home(request):
    context = {
        'animals': [
            {'name': "dog",
             'img': 'https://en.wiktionary.org/wiki/dog#/media/File:YellowLabradorLooking.jpg'
             },
            {'name': "cat",
             'img': 'https://en.wikipedia.org/wiki/Cat#/media/File:Felis_catus-cat_on_snow.jpg'
             }
        ]
    }
    return render(request, 'blog/home.html', context)
