from django.shortcuts import render
from django.http import HttpResponse as HR
from django.http import JsonResponse as JR

# Create your views here.


def home(request):
    return render(request,'blog/home.html')
