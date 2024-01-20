from django import forms 
from .models import CustomUser 
from django.contrib.auth.forms import UserCreationForm 

class UserForm(UserCreationForm): 
    first_name = forms.CharField(required=True, label="الاسم الأول")
    last_name = forms.CharField(required=True, label="الاسم الأخير")
    email = forms.EmailField(required=True, label="الايميل") 
    # sex = forms.CharField(widget=forms.Select, required=True, label='الجنس')
    id_number = forms.CharField(max_length=10, label='رقم الهوية', required=True)
    phone_number = forms.CharField(max_length=12, required=True, label="رقم الجوال", help_text="سيصلك رمز على هذا الرقم لذلك تأكد من الرقم") 
    class Meta: 
        model = CustomUser 
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 
            'sex', 'id_number', 'phone_number'
        ]


