from home.views import index , person , login , PersonView, PeopleViewSet# Import the index view from home app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')
urlpatterns = router.urls

urlpatterns = [
    path('index/', index, name='index'),  # Add a URL pattern for the index view
    path('person/', person),
    path('login/', login),
    path('persons/', PersonView.as_view()),  # URL for the PersonView class-based view
    path('', include(router.urls)),  # Include the router URLs
]  