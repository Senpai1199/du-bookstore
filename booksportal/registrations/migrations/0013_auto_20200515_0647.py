# Generated by Django 3.0.6 on 2020-05-15 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0012_auto_20200515_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookset',
            name='semester',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
