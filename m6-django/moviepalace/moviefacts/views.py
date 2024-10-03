from django.shortcuts import render

released_base = 'released_base.html'

def citizen_kane(request):
    context = {"movie": "Citizen Kane", "year": 1941}
    return render(request, released_base, context)

def casablanca(request):
    context = {"movie": "Casablanca", "year": 1942}
    return render(request, released_base, context)

def maltese_falcon(request):
    context = {"movie": "Maltese Falcon", "year": 1941}
    return render(request, "falcon.html", context)