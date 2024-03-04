from django.contrib import admin
from .models import Property, PropertyImage, Report, PropertyDepartment, Favourite

# Register your models here.

admin.site.register(PropertyDepartment) 
admin.site.register(PropertyImage)   
admin.site.register(Report)   
admin.site.register(Favourite)

class PropertyAdmin(admin.ModelAdmin): 
    model = Property
    search_fields = ('number', 'interface')

admin.site.register(Property, PropertyAdmin) 