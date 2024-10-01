from django.urls import path
from palindrome import views

urlpatterns = [
    path("", views.home, name='home'),
]