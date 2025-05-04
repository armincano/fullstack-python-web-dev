from django.shortcuts import render, redirect
from .forms import ClienteForm, ReservaForm
from .models import Cliente, Mesa, Reserva

def reservar(request):
    if request.method == 'POST':
        
        if request.POST.get('mesa'):
            pass
        
        if request.POST.get('hora'):
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            cantidad_personas = request.POST.get('cantidad_personas')
            reservas_libres = Reserva.objects.filter(fecha__exact=fecha ,capacidad__gte=cantidad_personas, hora__)
            reserva_form = ReservaForm(request.POST)
            reserva_form.fields['mesa'].queryset = mesas_libres
            context = {"reserva_form": reserva_form}
            return render(request, 'reserva_mesa/reservar.html', context)
        #     id_hora = request.POST.get('id_hora')
        #     mesa = Mesa.objects.get(id=id_hora)
        #     context = {"mesa": mesa, "reserva_form": ReservaForm()}
        #     return render(request, 'reserva_mesa/reservar.html', context)
            
        # form = ReservaForm(request.POST)
        # if form.is_valid():
        #     reserva = form.save(commit=False)
        #     reserva.save()
        #     mesa = reserva.mesa
        #     mesa.ocupada = True
        #     mesa.save()
        #     return redirect('reserva_mesa:reservar')
        
        rut = request.POST.get('rut')
        cliente = Cliente.objects.filter(rut=rut).first()
        if cliente is None:
            return redirect('reserva_mesa:crear_cliente')
        else:
            context = {"cliente": cliente}
            return render(request, 'reserva_mesa/reservar.html', context)
    
    return render(request, 'reserva_mesa/reservar.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_mesa:reservar')
    context = {"crear_cliente_form": ClienteForm()}
    return render(request, 'reserva_mesa/crear_cliente.html', context)