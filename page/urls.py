from django.urls import path 
from .views import * 

app_name = 'page' 

urlpatterns = [
    path('', index, name='index'), 
    path('about/', about, name='about'), 
    path('property-owners/', property_owners, name='property-owners'),
    path('request-contract/', request_contract, name='request-contract'),
    path('favourites/', favourites, name='favourites'),
]