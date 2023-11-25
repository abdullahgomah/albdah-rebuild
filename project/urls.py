
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings

from accounts.views import custom_login, signup, authenticate_page, send_otp

urlpatterns = [
    path('markdownx/', include('markdownx.urls')),
    path('login/', custom_login, name='custom-login'), 
    path('signup/', signup, name='signup'),
    path('auth/', authenticate_page, name='authenticate'), 
    path('auth/sendotp', send_otp, name='send-otp'), 
    path('accounts/', include('accounts.urls', namespace='accounts')), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('admin/', admin.site.urls),
    path('', include('page.urls', namespace='page')), 
    path('maps/', include('maps.urls', namespace='maps')), 
    path('property/', include('property.urls', namespace='property')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
