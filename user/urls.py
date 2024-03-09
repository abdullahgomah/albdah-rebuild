from django.urls import path 
from .views import * 
from django.contrib.auth import views as auth_views 
app_name= 'user' 


urlpatterns = [
    path('before-register/', before_register, name='before-register'),
    path('user-register/', user_register, name='user-register'), 
    path('office-register/', office_register, name='office-register'),
    path('markter-register/', markter_register, name='markter-register'), 
    path('user-login/', user_login, name='user-login'), 
    path('logout/', custom_logout, name='custom-logout'), 
    path('verify-phone-number/', verify_phone_number, name="verify-phone-number"),
    path('check-otp/', check_otp, name='check-otp'), 
    path('user-verified/', user_verified, name='user-verified'),
    path('profile/', profile, name='profile'), 
    path('profile_summary/', profile_summary, name='profile_summary'),
    path('my-ads/', my_ads, name='my-ads'), 
]