# Generated by Django 5.0.7 on 2024-07-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_created_devices_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='last_query',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
