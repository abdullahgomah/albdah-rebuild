from django.db import models
from accounts.models import User
import random 

# Create your models here.
class Code(models.Model): 
    number = models.CharField(max_length=5, blank=True)
    user  = models.OneToOneField(User, on_delete=models.CASCADE) 

    def __str__(self): 
        return str(self.number) 
    
    def save(self, *args, **kwargs): 
        number_list = [x for x in range(10)]
        code_items = [] 
        for i in range(5): 
            n = random.choice(number_list) 
            code_items.append(n ) 

        code_string = "".join(str(item) for item in code_items)
        self.number = code_string 
        
        super().save(*args, **kwargs) 


class Otp(models.Model): 
    phone_number = models.CharField(max_length=20, verbose_name="رقم الجوال") 
    otp = models.CharField(max_length=6, verbose_name="الكود") 

    def save(self, *args, **kwargs): 
        number_list = [x for x in range(10) ]

        code_items = [] 
        for i in range(5): 
            n = random.choice(number_list) 
            code_items.append(n) 
        
        code_string = "".join(str(item) for item in code_items) 
        self.otp = code_string

        super().save(*args, **kwargs) 


    def __str__(self):
        return self.otp 