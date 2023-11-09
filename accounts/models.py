from django.db import models
from django.contrib.auth.models import AbstractUser
from property.models import Property


# Create your models here.


class User(AbstractUser): 
    phone_number = models.CharField(max_length=25, unique=True)  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/', verbose_name='صورة الملف الشخصي', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    

    class Meta:
        verbose_name='ملف شخصي'
        verbose_name_plural ='الملفات الشخصية'



class Favourite(models.Model): 
    property = models.ForeignKey(Property, on_delete=models.CASCADE) 
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=True ,blank=True) 
    date  = models.DateTimeField(auto_now_add=True) 

