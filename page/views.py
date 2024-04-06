from django.shortcuts import render
from property.models import * 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *

# Create your views here.


def index(request): 

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')


    v = Visitor.objects.first()
    v.home +=1 
    v.save() 

    all_properties = Property.objects.all()[::-1]
    paginator = Paginator(all_properties, 10) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 

    next_page_obj = paginator.get_page(page_obj.number+1)
    next_five_pages = [page_obj]
    for i in range(5): 
        p = paginator.get_page(page_obj.number +i+1)  
        if page_obj.number +i+1 > paginator.num_pages: 
            break 
        else: 
            next_five_pages.append(p) 

    if page_obj.number == paginator.num_pages: 
        next_five_pages = [page_obj] 
        for i in range(page_obj.number-1, page_obj.number-1-5, -1):
            if i == 0: 
                break 
            else: 
                p = paginator.get_page(i) 
                print(p) 
                next_five_pages.append(p)
        next_five_pages.reverse()

    context = {
        'all_properties': all_properties, 
        'page_obj': page_obj, 
        'paginator': paginator,
        'pages': paginator.num_pages,
        'next_five':next_five_pages, 
        'visits': v,
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



def property_owners(request): 
    info  = PropertyOwner.objects.first() 
    context = {
        'property_owner_info': info.text,
    } 
    return render(request, 'pages/property-owners.html', context)
