# Generated by Django 5.0.1 on 2024-02-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الاسم الاول والأخير'),
        ),
    ]