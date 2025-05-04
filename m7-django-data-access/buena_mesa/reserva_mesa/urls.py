from django.urls import path, include
from . import views

app_name = 'reserva_mesa'

urlpatterns = [
    path('', views.reservar, name="reservar"),
    path('crear_cliente/', views.crear_cliente, name="crear_cliente"),
]