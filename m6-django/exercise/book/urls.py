from django.urls import path
from book import views

urlpatterns = [
    path("", views.home, name='book'),
    path("book_list/", views.book_list, name='book_list'),
    path("input_book/", views.input_book, name='input_book'),
]