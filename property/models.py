from django.db import models
import random 
import string 
from markdownx.models import MarkdownxField

from django.contrib.auth.models import User 

# Create your models here.


RENT_TYPE_CHOICES = [
    ('yearly', "سنوي"),
    ('monthly', "شهري")
]


PROPERTY_TYPE_CHOICES = [
    ("apartment_rent", "شقة للايجار"), 
    ("floor_rent", "دور للايجار"), 
    ('villa_rent', 'فيلا للايجار'), 
    ('shop_rent', 'محل للايجار'), 
    ('resthouse_rent', "استراحة للايجار"), 
    ("commercial_office_rent", "مكتب تجاري للايجار"), 
    ("land_rent", "أرض للايجار"), 
    ("building_rent", "عمارة للايجار"), 
    ("branch_rent", "مستودع للايجار"), 
    ("furnished_apartment_rent", "شقة مفروشة للايجار") ,
    ("chalet_rent", "شاليه للايجار"), 
    ("chalet_sale", "شاليه للبيع"), 
    ('land_sale', "أرض للبيع"), 
    ('villa_sale', "فيلا للبيع"), 
    ("apartment_sale", "شقة للبيع"), 
    ("building_sale", "عمارة للبيع"), 
    ("resthouse_sale", "استراحة للبيع"), 
    ("farm_sale", "مزرعة للبيع"), 
    ("shop_sale", "محل للبيع"), 
    ("floor_sale", "دور للبيع")
]

INTERFACE_CHOICES = [
    ('شمالية', 'شمالية'),
    ('جنوبية', 'جنوبية'),
    ('غربية', 'غربية'),
    ('شرقية', 'شرقية'),
    ('شمالية شرقية', 'شمالية شرقية'),
    ('شمالية غربية', 'شمالية غربية'),
    ('جنوبية شرقية', 'جنوبية شرقية'),
    ('جنوبية غربية', 'جنوبية غربية')
]


def generate(): 
    # Generate 2 random numbers between 0 and 9
    random_numbers = ''.join(random.choice(string.digits) for _ in range(2))

# Generate 3 random characters (uppercase and lowercase letters)
    random_characters = ''.join(random.choice(string.ascii_letters) for _ in range(3))

# Combine the random numbers and characters
    random_value = random_numbers + random_characters

    return str(random_value) 



class PropertyDepartment(models.Model): 
    name = models.CharField(max_length=100, verbose_name="الاسم البرمجي") 
    display_name = models.CharField(max_length=100, verbose_name="الاسم الظاهر")
    
    class Meta: 
        verbose_name = "قسم عقار"
        verbose_name_plural = "أقسام العقارات"

    def __str__(self):
        return self.display_name 


class Property(models.Model): 
    agree = models.BooleanField(default=False, verbose_name="موافقة" )
    # profile = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    lat = models.CharField(max_length=200, null=True, blank=True) 
    lng = models.CharField(max_length=200, null=True, blank=True)  
    
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة", null=True, blank=True) 
    p_type = models.CharField(max_length=250, verbose_name="نوع العقار", null=True, blank=True , choices=PROPERTY_TYPE_CHOICES) 
    title = models.CharField(max_length=255, verbose_name="عنوان الإعلان", null=True, blank=True) 
    sale = models.BooleanField(default=False, verbose_name="للبيع", null=True, blank=True) 
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  

    neighborhood = models.CharField(max_length=250, verbose_name="الحي", null=True, blank=True) 
    city = models.CharField(max_length=250, verbose_name="المدينة", null=True, blank=True) 
    title = models.CharField(max_length=255, verbose_name="عنوان الإعلان", null=True, blank=True) 

    price = models.FloatField(verbose_name="السعر (ريال سعودي)", default=0) 
    space = models.IntegerField(verbose_name="المساحة (متر مربع)", default=0) 
    width = models.FloatField(verbose_name="العرض (متر)", blank=True, null=True) 
    length = models.FloatField(verbose_name="الطول (متر)", blank=True, null=True) 

    advertiser_relation = models.CharField(max_length=50, verbose_name="علاقة المعلن بالعقار")
    exclusive = models.BooleanField(default=False, verbose_name='حصري') 


    video = models.FileField(upload_to='rent/apartment/video', verbose_name="فيديو", null=True, blank=True)
    interface = models.CharField(max_length=100, verbose_name="الواجهة", choices=INTERFACE_CHOICES, null=True, blank=True) 
    stores_count = models.CharField(default=0, verbose_name="عدد المحلات", max_length=10, null=True, blank=True)
    apartments_count = models.CharField(default=0, verbose_name="عدد الشقق", max_length=10, null=True, blank=True)

    street_width = models.FloatField(verbose_name="عرض الشارع", null=True, blank=True)  
    rooms = models.CharField(max_length=10, verbose_name="الغرف", null=True, blank=True) 

    lounges = models.CharField(max_length=10, verbose_name="الصالات", null=True, blank=True) 
    wells = models.CharField(max_length=10, verbose_name="عدد الآبار", null=True, blank=True) 
    trees = models.CharField(max_length=10, verbose_name="عدد الأشجار", null=True, blank=True) 
    
    bathroom = models.CharField(max_length=10, verbose_name="عدد دورات المياه", null=True, blank=True) 
    
    floor = models.CharField(max_length=200, verbose_name="الدور", null=True, blank=True) 

    property_age = models.CharField(max_length=200, verbose_name="عمر العقار", null=True, blank=True)  

    families = models.BooleanField(default=False, verbose_name="عوائل") 

    single = models.BooleanField(default=False, verbose_name='عزاب') 

    rent_type = models.CharField(max_length=50, choices=RENT_TYPE_CHOICES, verbose_name="نوع الإيجار", null=True, blank=True) 
    purpose = models.CharField(max_length=100, verbose_name="الغرض", null=True, blank=True)


    description = models.TextField(verbose_name="وصف العقار", default="   ", null=True, blank=True) 
    description = MarkdownxField(null=True, blank=True)

    furnished = models.BooleanField(default=False, verbose_name="مؤثثة") 

    kitchen = models.BooleanField(default=False, verbose_name="مطبخ")

    extenstion = models.BooleanField(default=False, verbose_name="ملحق")

    car_entrance= models.BooleanField(default=False, verbose_name="مدخل سيارة")

    elevator = models.BooleanField(default=False, verbose_name="مصعد كهربائي") 
    
    ac = models.BooleanField(default=False, verbose_name="مكيف")

    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    private_surface =models.BooleanField(default=False, verbose_name="سطح خاص")

    in_villa = models.BooleanField(default=False, verbose_name="في فيلا")
    two_enternace = models.BooleanField(default=False, verbose_name="مدخلين")

    private_enternace = models.BooleanField(default=False, verbose_name="مدخل خاص")

    driver_room = models.BooleanField(default=False, verbose_name="غرفة سائق") 
    maid_room = models.BooleanField(default=False, verbose_name="غرفة خادمة")

    duplex = models.BooleanField(default=False, verbose_name='دوبلكس')

    basement = models.BooleanField(default=False, verbose_name="قبو") 

    yard = models.BooleanField(default=False, verbose_name="حوش") 

    hair_tent_house = models.BooleanField(default=False, verbose_name="بيت شعر")

    pool = models.BooleanField(default=False, verbose_name="مسبح")
    football_field = models.BooleanField(default=False, verbose_name="ملعب كرة قدم")
    volly_field = models.BooleanField(default=False, verbose_name="ملعب كرة طائرة")

    hair_tent_house = models.BooleanField(default=False, verbose_name="بيت شعر")

    amusement = models.BooleanField(default=False, verbose_name="ملاهي")

    family_part = models.BooleanField(default=False, verbose_name="قسم عوائل")

    monthly_payment = models.BooleanField(default=False, verbose_name="دفع شهري") 
    quarterly_payment = models.BooleanField(default=False, verbose_name='دفع ربع سنوي') 
    semi_annual_payment= models.BooleanField(default=False, verbose_name="دفع نصف سنوي") 
    annual_payment = models.BooleanField(default=False, verbose_name="دفع سنوي") 

    def __str__(self):
        return str(self.title )

    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        
        if not self.title: 
            start = "" 
            mid = "" 

            if self.p_type.startswith("apartment"):
                start = "شقة" 
            elif self.p_type.startswith("floor"): 
                start = "دور" 
            elif self.p_type.startswith("villa"): 
                start = "فيلا" 
            elif self.p_type.startswith("shop"): 
                start = "محل" 
            elif self.p_type.startswith("resthouse"): 
                start = 'استراحة' 
            elif self.p_type.startswith("commercial_office"): 
                start = 'مكتب تجاري'
            elif self.p_type.startswith("land"): 
                start = 'أرض' 
            elif self.p_type.startswith("building"): 
                start = "عمارة" 
            elif self.p_type.startswith("branch"): 
                start = "مستودع" 
            elif self.p_type.startswith("furnished_apartment"): 
                start = "شقة مفروشة" 
            elif self.p_type.startswith("chalet"): 
                start = "شاليه"      
            elif self.p_type.startswith("farm"): 
                start = "مزرعة"      

            if self.sale == 1: 
                mid = "للبيع" 
            else: 
                mid = "للإيجار"   


            sentence = f"{start} {mid} في {self.city} في {self.neighborhood}"

            self.title = sentence 
        super(Property, self).save(*args, **kwargs)

    class Meta: 
        verbose_name = 'عقار'
        verbose_name_plural = 'عقارات' 


class PropertyImage(models.Model): 
    property = models.ForeignKey( Property, on_delete=models.CASCADE, related_name='imgs' , verbose_name="العقار")
    img = models.ImageField(upload_to="property/images/")
    main = models.BooleanField(default=0, null=True, blank=True, verbose_name="صورة رئيسية" ) 

    def __str__(self):
        return str(self.property.number  ) 


    class Meta: 
        verbose_name = 'صورة عقار'
        verbose_name_plural = "صور العقارات"



class Report(models.Model):
    ad = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="الإعلان") 
    number = models.CharField(max_length=40, verbose_name="رقم الإعلان", default="") 
    date = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'إبلاغ'
        verbose_name_plural = 'البلاغات'

    def __str__(self):
        return f"{self.ad} {self.date}"
    

