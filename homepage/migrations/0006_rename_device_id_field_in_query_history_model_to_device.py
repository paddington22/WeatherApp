# Generated by Django 5.0.7 on 2024-07-19 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_rename_devices_model_to_device'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queryhistory',
            old_name='device_id',
            new_name='device',
        ),
    ]
