from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, world! this home page')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('Hello, world! this is about page')

def contact(request):
    return HttpResponse('Hello, world! this is contact page')