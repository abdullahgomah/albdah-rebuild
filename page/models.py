from django.db import models

# Create your models here.
class Home(models.Model): 
    title = models.CharField(max_length=200, verbose_name="العنوان الرئيسي") 
    slogan = models.TextField(verbose_name="الجملة الفرعية")
    snapchat = models.TextField(verbose_name="رابط سناب شات", null=True, blank=True) 
    whatsapp = models.TextField(verbose_name="رابط واتساب", null=True, blank=True) 
    tiktok = models.TextField(verbose_name="رابط تيكتوك", null=True, blank=True) 
    location = models.TextField(verbose_name="رابط لوكيشن", null=True, blank=True) 

    def __str__(self):
        return str(self.title[:10])