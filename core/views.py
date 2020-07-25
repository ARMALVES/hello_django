from django.shortcuts import render, HttpResponse

# Create your views here.

#def hello(request):
#    return HttpResponse('<h1>Hello World!</h1>')

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos.</h1> '.format(nome, idade))