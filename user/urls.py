from django.urls import path 
from .views import * 
app_name= 'user' 

urlpatterns = [
    path('before-register/', before_register, name='before-login'),
    path('user-register/', user_register, name='user-register'), 
    path('user-login/', user_login, name='user-login'), 
    path('logout/', custom_logout, name='custom-logout'), 
]