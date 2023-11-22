from django.urls import path 
from .views import * 

app_name = 'maps' 

urlpatterns = [
    path('search', search_with_map, name='search-with-map'), 
]