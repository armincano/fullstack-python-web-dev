from django.shortcuts import render
from django.http import HttpResponse

def commands(request):
    return render(request, "book/commands.html")

def index(request):
    return render(request, "book/index.html")