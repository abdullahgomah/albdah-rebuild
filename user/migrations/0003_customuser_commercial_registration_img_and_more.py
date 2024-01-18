# Generated by Django 4.2.6 on 2024-01-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_fal_license_customuser_office_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='commercial_registration_img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/commercial-registrations/', verbose_name='صورة السجل التجاري'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fal_license',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/fal/', verbose_name='صورة رخصة فال'),
        ),
    ]