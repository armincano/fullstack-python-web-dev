from django.urls import path
from book import views

app_name = "book"

urlpatterns = [
    path("", views.book, name='book'),
    path("book_list/", views.book_list, name='book_list'),
    path("input_book/", views.input_book, name='input_book'),
]