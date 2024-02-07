from django.db import models

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