from django.shortcuts import render
from .models import * 

# Create your views here.
def before_login(request): 
    context = {} 
    return render(request, 'user/before-login.html', context)