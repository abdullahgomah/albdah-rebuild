# Generated by Django 4.2.6 on 2024-01-10 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_alter_property_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='p_type',
            field=models.CharField(blank=True, choices=[('apartment_rent', 'شقة للايجار'), ('floor_rent', 'دور للايجار'), ('villa_rent', 'فيلا للايجار'), ('shop_rent', 'محل للايجار'), ('resthouse_rent', 'استراحة للايجار'), ('commercial_office_rent', 'مكتب تجاري للايجار'), ('land_rent', 'أرض للايجار'), ('building_rent', 'عمارة للايجار'), ('branch_rent', 'مستودع للايجار'), ('furnished_apartment_rent', 'شقة مفروشة للايجار'), ('chalet_rent', 'شاليه للايجار'), ('chalet_sale', 'شاليه للبيع'), ('land_sale', 'أرض للبيع'), ('villa_sale', 'فيلا للبيع'), ('apartment_sale', 'شقة للبيع'), ('building_sale', 'عمارة للبيع'), ('resthouse_sale', 'استراحة للبيع'), ('farm_sale', 'مزرعة للبيع'), ('shop_sale', 'محل للبيع'), ('floor_sale', 'دور للبيع')], max_length=250, null=True, verbose_name='نوع العقار'),
        ),
    ]
