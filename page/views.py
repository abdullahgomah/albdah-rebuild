from django.shortcuts import render
from property.models import * 
from accounts.models import * 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def index(request): 
    all_properties = Property.objects.all()[::-1]
    page = request.GET.get("page") 
    print(page) 
    context = {
        'all_properties': all_properties
    } 
    return render(request, 'pages/index.html', context)


def about(request): 
    context = {} 
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

