from django.contrib import admin
from .models import Home, About, PropertyOwner, PropertyDetails, Visitor, Complain, PrivacyPolicy

admin.site.register(Home) 
admin.site.register(About) 
admin.site.register(PropertyOwner) 
admin.site.register(PropertyDetails) 
admin.site.register(Visitor)
admin.site.register(Complain)
admin.site.register(PrivacyPolicy)

# Register your models here.

#tel 
# whatsapp_tel