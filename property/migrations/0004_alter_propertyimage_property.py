# Generated by Django 4.2.6 on 2023-11-02 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_propertyimage_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='property.property'),
        ),
    ]
