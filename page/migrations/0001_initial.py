# Generated by Django 5.0.1 on 2024-04-30 15:41

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_text', models.CharField(max_length=255, verbose_name='الجملة الرئيسية')),
                ('sub_text', models.TextField(blank=True, null=True, verbose_name='النص الفرعي')),
            ],
            options={
                'verbose_name': 'من نحن',
                'verbose_name_plural': 'من نحن',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='العنوان الرئيسي')),
                ('phone', models.CharField(max_length=20, verbose_name='رقم الجوال')),
                ('slogan', models.TextField(blank=True, null=True, verbose_name='الجملة الفرعية')),
                ('snapchat', models.TextField(blank=True, null=True, verbose_name='رابط سناب شات')),
                ('whatsapp', models.TextField(blank=True, null=True, verbose_name='رابط واتساب')),
                ('tiktok', models.TextField(blank=True, null=True, verbose_name='رابط تيكتوك')),
                ('location', models.TextField(blank=True, null=True, verbose_name='رابط لوكيشن')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=25, null=True)),
                ('whatsapp_tel', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name': 'صفحة تفاصيل الإعلان',
                'verbose_name_plural': 'صفحة تفاصيل الإعلان',
            },
        ),
        migrations.CreateModel(
            name='PropertyOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', django_ckeditor_5.fields.CKEditor5Field()),
                ('a', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'أصحاب العقار',
                'verbose_name_plural': 'أصحاب العقار',
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Visitor',
                'verbose_name_plural': 'Visitors',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
