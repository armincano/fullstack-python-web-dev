from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages

def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    
    context = {"form": form}        
    return render(request, "../templates/signup.html", context)

def user_login(request):
    
    for message in messages.get_messages(request):
        if message.message == "no permission":
            context = {"error": "no permission"}
            return render(request, "../templates/login.html", context)
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            context = {"error": "wrong credentials"}
            return render(request, "../templates/login.html", context)
    
    return render(request, "../templates/login.html")


def user_logout(request):
    logout(request)
    return redirect("index")


def index(request):
    return render(request, "../templates/index.html")
