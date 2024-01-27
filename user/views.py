from django.shortcuts import render, redirect
from .models import * 
from .forms import * 
from .backends import CustomIdBackend
from django.contrib.auth import login, logout


# Create your views here.
def before_register(request): 
    context = {} 
    return render(request, 'user/before-login.html', context)


def user_register(request): 
    form = UserForm()

    if request.POST: 
        form = UserForm(request.POST) 
        if form.is_valid(): 
            form.save(commit=False) 
            form.instance.role = 'user' 
            form.save() 

    context = {
        'form': form 
    }
    return render(request, 'user/signup.html', context)


def office_register(request): 
    form = OfficeRegister() 

    if request.POST: 
        form = OfficeRegister(request.POST) 
        if form.is_valid(): 
            form.save(commit=False) 
            form.instance.role = 'real_estate_office'
            form.save() 
        
        

    context ={ 
        'form': form 
    }

    return render(request, 'user/signup.html', context)
    

def markter_register(request): 
    form = MarkterRegister() 

    if request.POST: 
        form = MarkterRegister(request.POST) 
        if form.is_valid(): 
            form.save(commit=False) 
            form.instance.role = 'real_estate_marketer' 
            form.save() 
            

    context = {
        'form': form 
    }

    return render(request, 'user/signup.html', context)

def user_login(request):

    if request.POST: 
        id_number = request.POST.get('id_number_input') 
        password= request.POST.get('password_input') 
        
        user = CustomIdBackend().authenticate(request, id_number=id_number, password=password) 

        if user is not None: 
            login(request, user=user, backend='user.backends.CustomIdBackend')
            return redirect('page:index')


    context = {
    } 
    return render(request, 'user/user-login.html', context)


def custom_logout(request): 
    logout(request) 

    return redirect('page:index') 