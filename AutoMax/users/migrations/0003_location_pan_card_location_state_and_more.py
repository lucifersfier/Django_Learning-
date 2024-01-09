# Generated by Django 5.0.1 on 2024-01-09 19:58

import localflavor.in_.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='pan_card',
            field=localflavor.in_.models.INPANCardNumberField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.in_.models.INStateField(default='Delhi', max_length=2),
        ),
        migrations.AlterField(
            model_name='location',
            name='address1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
