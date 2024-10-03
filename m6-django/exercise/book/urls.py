from django.urls import path
from book import views

urlpatterns = [
    path("", views.home, name='book'),
    path("book_list/", views.book_list, name='book_list')
]