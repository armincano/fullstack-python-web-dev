from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import logging
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def home(request):
    return render(request, "../templates/home.html")


def navbar(request):
    return render(request, "../templates/navbar.html")


def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"form": form}
    return render(request, "../templates/signup.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Invalid username or password")
    return render(request, "../templates/login.html")
