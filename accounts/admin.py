from django.contrib import admin
from .models import User, Profile, Favourite
# from .models import Profile
# Register your models here.

# admin.site.register(Profile) 


class UserAdmin(admin.ModelAdmin): 
    search_fields = ['username', 'phone_number']

admin.site.register(User, UserAdmin)


class FavouriteAdmin(admin.ModelAdmin): 
    search_fields = ['date', 'profile'] 

admin.site.register(Favourite, FavouriteAdmin) 

