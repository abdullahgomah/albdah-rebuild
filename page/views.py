from django.shortcuts import render
from property.models import * 

# Create your views here.


def index(request): 
    all_properties = Property.objects.all()
    context = {
        'all_properties': all_properties
    } 
    return render(request, 'pages/index.html ', context)


def about(request): 
    context = {} 
    return render(request, 'pages/about.html', context)


def request_contract(request): 
    context = {}
    return render(request, 'pages/request_contract.html', context)