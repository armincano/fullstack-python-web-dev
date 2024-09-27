from django.shortcuts import render

def commands(request):
    return render(request, "book/commands.html")