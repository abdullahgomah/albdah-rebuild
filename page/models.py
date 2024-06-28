from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Home(models.Model): 
    title = models.CharField(max_length=200, verbose_name="العنوان الرئيسي") 
    phone = models.CharField(max_length=20, verbose_name="رقم الجوال") 
    slogan = models.TextField(verbose_name="الجملة الفرعية", null=True, blank=True)
    snapchat = models.TextField(verbose_name="رابط سناب شات", null=True, blank=True) 
    whatsapp = models.TextField(verbose_name="رابط واتساب", null=True, blank=True) 
    tiktok = models.TextField(verbose_name="رابط تيكتوك", null=True, blank=True) 
    location = models.TextField(verbose_name="رابط لوكيشن", null=True, blank=True) 
    
    def __str__(self):
        return str(self.title[:10])
    

class About(models.Model):
    main_text = models.CharField(max_length=255, verbose_name="الجملة الرئيسية")
    sub_text = models.TextField(verbose_name="النص الفرعي", null=True, blank=True) 

    class Meta:
        verbose_name='من نحن'
        verbose_name_plural='من نحن'

class PropertyOwner(models.Model): 
    text = CKEditor5Field(config_name="extends")
    a = models.CharField(null=True, blank=True, max_length=100) 

    class Meta: 
        verbose_name = "أصحاب العقار"
        verbose_name_plural = "أصحاب العقار"


class Visitor(models.Model):
    home = models.IntegerField(default=0) 
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'

    
class PropertyDetails(models.Model): 
    tel = models.CharField(max_length=25, blank=True, null=True) 
    whatsapp_tel = models.CharField(max_length=25, blank=True, null=True) 

    def __str__(self): 
        return str(self.tel) 
    
    class Meta: 
        verbose_name = "صفحة تفاصيل الإعلان" 
        verbose_name_plural = 'صفحة تفاصيل الإعلان'


class Complain(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="الاسم")
    description = models.TextField(verbose_name="التفاصيل") 
    date_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
       
       if not self.name :
           self.name = str(self.date_time) 
       
       super(Complain, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'شكوى'
        verbose_name_plural = 'الشكاوي'

class PrivacyPolicy(models.Model): 
    text= CKEditor5Field(config_name="extends")

    class Meta: 
        verbose_name= "سياسة الخصوصية"
        verbose_name_plural = "سياسة الخصوصية" 