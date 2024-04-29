from django.contrib import admin
from .models import * 
from django.contrib.auth import authenticate
from .forms import * 


# Register your models here.


class CustomUserAdmin(admin.ModelAdmin): 
    model= CustomUser 
    list_display = ('phone_number', 'id_number')


admin.site.register(CustomUser, CustomUserAdmin) 

