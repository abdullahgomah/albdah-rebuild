# Generated by Django 4.2.6 on 2023-11-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_propertyimage_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='lat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='lng',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
