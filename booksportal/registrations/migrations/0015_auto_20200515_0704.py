# Generated by Django 3.0.6 on 2020-05-15 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0014_auto_20200515_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
