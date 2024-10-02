from django.shortcuts import render

def home(request):
    return render(request, "../templates/home.html")

def navbar(request):
    return render(request, "../templates/navbar.html")