from django.shortcuts import render, redirect
from django.http import HttpResponse, request

# Create your views here.

def index(request):
   return render(request, 'musicapp/index.html')
   #return render(request, 'home/home.html', context)

def blog(request):
   #return render(request=request, template_name='musicapp/blog.html')
   return render(request, 'musicapp/blog.html')


def contact(request):
   return render(request, 'musicapp/contact.html')

def elements(request):
   return render(request, 'musicapp/elements.html')

def event(request):
   return render(request, 'musicapp/event.html')

def login(request):
   #return render(request=request, template_name='musicapp/login.html')
   return render(request, 'musicapp/login.html')


def albumsstore(request):
   return render(request, 'musicapp/albums-store.html')
