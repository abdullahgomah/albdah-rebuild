# Generated by Django 4.2.6 on 2024-01-11 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_propertydepartment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertydepartment',
            options={'verbose_name': 'قسم عقار', 'verbose_name_plural': 'أقسام العقارات'},
        ),
    ]