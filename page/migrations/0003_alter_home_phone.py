# Generated by Django 4.2.6 on 2024-02-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_home_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='رقم الجوال'),
        ),
    ]