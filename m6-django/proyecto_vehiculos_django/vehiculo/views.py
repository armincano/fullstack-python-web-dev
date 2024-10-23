from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def add(request):
    if not request.user.has_perm('vehiculo.add_vehiculo'):
        messages.error(request, "no permission")
        return redirect('/login')
    
    form = VehiculoForm(request.POST or None)
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {"form": form}
    return render(request, 'add.html', context)

@login_required
def catalog(request):
    context = {"vehiculos": Vehiculo.objects.all()}
    return render(request, 'catalog.html', context)