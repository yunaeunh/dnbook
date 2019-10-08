# Generated by Django 2.2.5 on 2019-09-27 06:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmap', '0002_auto_20190927_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstore',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
