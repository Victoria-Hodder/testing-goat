from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse(request, 'home.html') # AttributeError: 'HttpRequest' object has no attribute '_stream'