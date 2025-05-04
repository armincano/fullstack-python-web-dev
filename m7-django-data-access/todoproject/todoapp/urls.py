from django.urls import path
from . import views

urlpatterns = [
    path('', views.createTodoView, name='todo_url'),
    path('show/', views.showTodoView, name='show_url'),
    path('up/<int:f_id>', views.updateTodoView, name= 'update_url'),
    path('del/<int:f_id>', views.deleteTodoView, name= 'delete_url'),
]