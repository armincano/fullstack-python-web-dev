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

def psycho(request):
    context = {
        "movie": "Psycho",
        "year": 1960,
        "is_scary": True,
        "color": False,
        "tomato_meter": 96,
        "tomato_audience": 95,
    }
    return render(request, "psycho.html", context)

def listing(request):
    context = {
        "movies": [
            (
                "Citizen Kane",   # Movie
                1941,             # Year
            ),
            (
                "Casablanca",
                1942,
            ),
            (
                "Psycho",
                1960,
            ),
        ]
    }
    return render(request, "listing.html", context)