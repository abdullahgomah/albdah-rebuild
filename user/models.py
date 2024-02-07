from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

SEX_CHOICES = (
    ('m', "ذكر"), 
    ("f", "أنثى")
)


ROLE_CHOICES = (
    ('user', "مستخدم"), 
    ("real_estate_marketer", "مسوق عقاري"), 
    ("real_estate_office", 'مكتب عقاري') 
)

class CustomUser(AbstractUser):
    first_name = None  
    last_name = None 
    name = models.CharField(max_length=255, verbose_name="الاسم الاول والأخير", null=True, blank=True)
    username = models.CharField(max_length=150 ,blank=True, unique=True)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, verbose_name='نوع المستخدم', null=True, blank=True)
    id_number = models.CharField(max_length=10, verbose_name="رقم الهوية", null=True, blank=True, unique=True) 
    sex = models.CharField(max_length=200, verbose_name='الجنس', choices=SEX_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name="رقم الجوال", null=True, blank=True, unique=True) 
    phone_number_verify_status = models.BooleanField(default=False, null=True, blank=True)
    fal_license = models.ImageField(upload_to='uploads/fal/', null=True, blank=True, verbose_name="صورة رخصة فال") 
    office_name = models.CharField(max_length=200, verbose_name="اسم المكتب كما هو مكتوب في السجل التجاري", null=True, blank=True) 
    commercial_registration_img = models.ImageField(upload_to='uploads/commercial-registrations/', verbose_name='صورة السجل التجاري', null=True, blank=True)

    def __str__(self):
        return str(self.id_number) 

    # الجنس 
    # رقم الجوال 
    # السجل التجاري
    # رقم الاقامة 
    # صورة رخصة فال  
    # اسم المكتب كما في السجل التجاري 