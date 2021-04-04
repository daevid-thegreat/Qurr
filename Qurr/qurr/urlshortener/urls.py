from django.urls import path
from .views import Home, createShortURL, redirect

urlpatterns = [
    path('', Home, name='Home'),
    path('create/', createShortURL, name='Create'),
    path('<str:url>', redirect, name='Redirect'),
]
