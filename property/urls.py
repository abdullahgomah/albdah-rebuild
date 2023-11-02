from django.urls import path 
from .views import * 

app_name = 'property' 

urlpatterns = [
    path('<str:number>/details/', property_details, name='property-details'), 
    path('add-property/', add_property_interface, name='add-property-interface'), 
    path('add-property/new/<str:property_type>/', add_property, name='add-property')
]