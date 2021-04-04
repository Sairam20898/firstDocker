from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1 style="text-align:center;">Hello World!!</h1> \n <h1 style="text-align:center;">This is '
                        'Sairam </h1> \n <h1 style="text-align:center;"> This is my docker containerized application')
