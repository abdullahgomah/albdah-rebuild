# Generated by Django 5.0.1 on 2024-06-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='الاسم')),
                ('description', models.TextField(verbose_name='التفاصيل')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Complain',
                'verbose_name_plural': 'Complains',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
