from django.urls import path 
from .views import * 
app_name= 'user' 

urlpatterns = [
    path('before-login/', before_login, name='before-login'),
    path('user-register/', user_register, name='user-register'), 
]