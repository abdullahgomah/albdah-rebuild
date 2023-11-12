from django.shortcuts import render
from property.models import * 

# Create your views here.
def search_with_map(request): 
    properties = Property.objects.all()

    context = {
        'properties': properties
    }
    return render(request, 'maps/index.html', context)

