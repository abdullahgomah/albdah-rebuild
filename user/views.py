from django.shortcuts import render
from .models import * 
from .forms import * 

# Create your views here.
def before_login(request): 
    context = {} 
    return render(request, 'user/before-login.html', context)


def user_register(request): 
    form = UserForm()

    if request.POST: 
        form = UserForm(request.POST) 
        if form.is_valid(): 
            form.save() 


    context = {
        'form': form 
    }
    return render(request, 'user/signup.html', context)

