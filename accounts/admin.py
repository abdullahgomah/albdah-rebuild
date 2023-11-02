from django.contrib import admin
from .models import User 
# from .models import Profile

# Register your models here.

# admin.site.register(Profile) 


class UserAdmin(admin.ModelAdmin): 
    search_fields = ['username', 'phone_number']

admin.site.register(User, UserAdmin)