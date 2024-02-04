from django.shortcuts import render
from property.models import * 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *

# Create your views here.


def index(request): 
    all_properties = Property.objects.all()[::-1]
    paginator = Paginator(all_properties, 10) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 

    context = {
        'all_properties': all_properties, 
        'page_obj': page_obj, 
        'paginator': paginator,
    } 
    return render(request, 'pages/index.html', context)


def about(request): 
    about = About.objects.first() 
    context = {
        'about': about, 
    } 
    return render(request, 'pages/about.html', context)


def request_contract(request): 
    context = {}
    return render(request, 'pages/request_contract.html', context)



@login_required(login_url='/auth/')
def favourites(request):
    user = request.user 
    ads = Favourite.objects.filter(user=user)
    context = {
        'all_properties': ads
    } 
    return render(request, 'pages/favourites.html', context=context)

