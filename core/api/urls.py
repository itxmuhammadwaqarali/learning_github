from home.views import index , person , login # Import the index view from home app
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),  # Add a URL pattern for the index view
    path('person/', person),  # Admin URL
    path('login/', login),  # Admin URL
]