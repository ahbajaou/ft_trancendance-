# Generated by Django 5.1 on 2024-09-01 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0006_user_otp_user_otp_expiry_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_expiry_time',
        ),
    ]
