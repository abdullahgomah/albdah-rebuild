from django.contrib import admin
from .models import Property, PropertyImage, Report, PropertyDepartment, Favourite
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

admin.site.register(PropertyDepartment) 
admin.site.register(Report)   
admin.site.register(Favourite)



def make_draft(modeladmin, request, queryset): 
    queryset.update(draft=True) 
    modeladmin.message_user(request, _('تم تحويل الإعلانات المحددة إلى مسودة'))

make_draft.short_description = "تحويل الإعلانات المحددة إلى مسودة"


class PropertyAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    model = Property
    search_fields = ('id', 'number', 'interface', 'title')
    list_filter = ('draft', 'interface', )

    list_display = ('title', 'id',) 


    actions = [make_draft]

admin.site.register(Property, PropertyAdmin)




class PropertyImageAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    model = PropertyImage

admin.site.register(PropertyImage, PropertyImageAdmin)



