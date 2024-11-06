from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def catalogo(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_del_proyecto:catalogo')
    productos = Producto.objects.all()
    context = {"productos": productos, "form": ProductoForm()}
    return render(request, 'productos_del_proyecto/catalogo.html', context)