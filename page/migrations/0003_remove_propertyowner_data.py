# Generated by Django 5.0.1 on 2024-02-13 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_propertyowner_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyowner',
            name='data',
        ),
    ]
