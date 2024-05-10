# Generated by Django 5.0.1 on 2024-05-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='fal_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='رقم رخصة فال'),
        ),
        migrations.AddField(
            model_name='property',
            name='license_num',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='رقم رخصة الإعلان'),
        ),
    ]
