from django.urls import path 
from .views import * 

app_name = 'property' 

urlpatterns = [
    path('<str:number>/details/', property_details, name='property-details'), 
    path('add-property/', add_property_interface, name='add-property-interface'), 
    path('add-property/new/<str:property_type>/', add_property, name='add-property'), 
    path('add-property/new/<str:offer_type>/<str:property_type>/', add_property, name='add-property-sell'), 
    path('ad-uploaded/', ad_uploaded, name='ad-uploaded'), 
    path('add-to-favourite/<str:property_number>/', add_to_favourite, name='add-to-favourite'), 
    path('report/<str:number>/', report_property, name='report-property'), 
    path('report/reported', show_reported, name='reported'), 
    path('filter/', filter_properties, name='filter-properties'), 
    path('filter-result/<str:p_type>/', filter_result, name='filter-result'), 
]