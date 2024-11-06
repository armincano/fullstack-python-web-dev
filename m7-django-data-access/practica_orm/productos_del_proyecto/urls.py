from django.urls import path
from . import views

app_name = "productos_del_proyecto"

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
]
