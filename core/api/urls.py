from home.views import index , person , login , PersonView # Import the index view from home app
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),  # Add a URL pattern for the index view
    path('person/', person),
    path('login/', login),
    path('persons/', PersonView.as_view()),  # URL for the PersonView class-based view
]