from django.urls import path
from palindrome import views

urlpatterns = [
    path("", views.home, name='home'),
    path("<str:word>/", views.is_palindrome, name="is_palindrome")
]