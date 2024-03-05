# Generated by Django 5.0.1 on 2024-03-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'مستخدم'), ('real_estate_marketer', 'مسوق عقاري'), ('real_estate_office', 'مكتب عقاري')], max_length=200, null=True, verbose_name='نوع المستخدم'),
        ),
    ]