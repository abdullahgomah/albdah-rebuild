from django.contrib import admin
from .models import Property, PropertyImage, Report, PropertyDepartment, Favourite
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(PropertyDepartment) 
admin.site.register(Report)   
admin.site.register(Favourite)

class PropertyAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    model = Property
    search_fields = ('id', 'number', 'interface', 'title')

    list_display = ('title', 'id',) 

admin.site.register(Property, PropertyAdmin)




class PropertyImageAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    model = PropertyImage

admin.site.register(PropertyImage, PropertyImageAdmin)

