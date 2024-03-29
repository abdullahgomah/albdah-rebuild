from django.contrib import admin
from .models import Property, PropertyImage, Report, PropertyDepartment, Favourite
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(PropertyDepartment) 
admin.site.register(PropertyImage)   
admin.site.register(Report)   
admin.site.register(Favourite)

class PropertyAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    model = Property
    search_fields = ('number', 'interface', 'title')

admin.site.register(Property, PropertyAdmin)

