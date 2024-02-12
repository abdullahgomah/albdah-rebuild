
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('markdownx/', include('markdownx.urls')), 
    path('user/', include('user.urls', namespace='user')) , 
    path('admin/', admin.site.urls),
    path('', include('page.urls', namespace='page')), 
    path('maps/', include('maps.urls', namespace='maps')), 
    path('property/', include('property.urls', namespace='property')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
