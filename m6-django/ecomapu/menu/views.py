from django.shortcuts import render
from menu.models import MenuItem

def index(request):
    context = {"menu_items": MenuItem.objects.all()}
    return render(request, "menu/index.html", context)
