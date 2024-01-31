from django import forms 
from .models import CustomUser 
from django.contrib.auth.forms import UserCreationForm 

class UserForm(UserCreationForm): 
    first_name = forms.CharField(required=True, label="الاسم الأول")
    last_name = forms.CharField(required=True, label="الاسم الأخير")
    email = forms.EmailField(required=True, label="الايميل") 
    id_number = forms.CharField(max_length=10, label='رقم الهوية', required=True)
    phone_number = forms.CharField(max_length=13, required=True, label="رقم الجوال", help_text="سيصلك رمز على هذا الرقم لذلك تأكد من الرقم") 
    # sex = forms.CharField(widget=forms.Select, required=True, label='الجنس')
    class Meta: 
        model = CustomUser 
        fields = [
            # 'username', 
            'first_name', 'last_name', 'email', 'password1', 'password2', 
            'sex', 'id_number', 'phone_number'
        ]


class OfficeRegister(UserCreationForm): 
    email = forms.EmailField(required=True, label="الايميل") 
    id_number = forms.CharField(max_length=10, label='رقم الهوية', required=True)
    office_name = forms.CharField(max_length=10, label='اسم المكتب كما هو مكتوب في السجل التجاري', required=True)
    phone_number = forms.CharField(max_length=13, required=True, label="رقم الجوال", help_text="سيصلك رمز على هذا الرقم لذلك تأكد من الرقم") 
    commercial_registration_img = forms.ImageField(required=True, label="صورة السجل التجاري", widget=forms.FileInput(attrs={'class': 'form-control' })) 
    class Meta: 
        model = CustomUser 
        fields = [
            # 'username', 
            'office_name', 
            'email', 
            'id_number',
            'phone_number',  
            'commercial_registration_img', 
            'password1', 
            'password2',
        ]

class MarkterRegister(UserCreationForm): 
    first_name = forms.CharField(required=True, label="الاسم الأول")
    last_name = forms.CharField(required=True, label="الاسم الأخير")
    email = forms.EmailField(required=True, label="الايميل") 
    id_number = forms.CharField(max_length=10, label='رقم الهوية', required=True)
    phone_number = forms.CharField(max_length=13, required=True, label="رقم الجوال", help_text="سيصلك رمز على هذا الرقم لذلك تأكد من الرقم") 
    fal_license = forms.ImageField(required=True, label="صورة رخصة فال", widget=forms.FileInput(attrs={'class': 'form-control' })) 

    class Meta: 
        model = CustomUser 
        fields = [
            'first_name', 
            'last_name', 
            # 'username', 
            'phone_number',
            'email', 
            'id_number', 
            'fal_license', 
            'sex',
            'password1', 
            'password2',    
        ]