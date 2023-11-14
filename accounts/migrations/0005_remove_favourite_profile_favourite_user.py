# Generated by Django 4.2.6 on 2023-11-08 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='profile',
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]