from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def index(request):
   return render(request, template_name='musicapp/index.html')

def blogview(request):
   return render(request, template_name='musicapp/blog.html')

def contactview(request):
   return render(request, template_name='musicapp/contact.html')

def elementsview(request):
   return render(request, template_name='musicapp/elements.html')

def eventview(request):
   return render(request, template_name='musicapp/events.html')

def login(request):
   return render(request, template_name='musicapp/login.html')

def albumsstoreview(request):
   return render(request, template_name='musicapp/albums-store.html')
