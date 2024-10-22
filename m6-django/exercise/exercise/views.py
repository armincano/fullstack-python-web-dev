from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
import logging
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def home(request):
    return render(request, "../templates/home.html")


def navbar(request):
    return render(request, "../templates/navbar.html")


def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"form": form}

    # Print the keys and attributes of the form fields
    field_keys = form.fields.keys()
    for key in field_keys:
        print(f"Field: {key}")
        field = form.fields[key]
        widget = field.widget
        print(f"  name: {key}")
        print(f"  label: {field.label}")
        print(f"Widget: {widget}")
        # Print the id_for_label of the widget
        print(f"  id_for_label: {widget.id_for_label(key)}")
        
        # Print each attribute of the widget
        widget_attributes = widget.__dict__.items()
        for attr_name, attr_value in widget_attributes:
            print(f"  {attr_name}: {attr_value}")
            
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

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return render(request, "../templates/logout.html")