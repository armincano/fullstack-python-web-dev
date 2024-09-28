from django.urls import path, include
from . import views

app_name="book"

urlpatterns = [
    path('commands/', views.commands, name='commands'),
    path('', views.index, name='index'),
]