
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('markdownx/', include('markdownx.urls')), 
    path('user/', include('user.urls', namespace='user')) , 
    path('admin/', admin.site.urls),
    path('', include('page.urls', namespace='page')), 
    path('maps/', include('maps.urls', namespace='maps')), 
    path('property/', include('property.urls', namespace='property')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
