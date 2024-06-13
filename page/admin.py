from django.contrib import admin
from .models import Home, About, PropertyOwner, PropertyDetails, Visitor, Complain

admin.site.register(Home) 
admin.site.register(About) 
admin.site.register(PropertyOwner) 
admin.site.register(PropertyDetails) 
admin.site.register(Visitor)
admin.site.register(Complain)

# Register your models here.

#tel 
# whatsapp_tel