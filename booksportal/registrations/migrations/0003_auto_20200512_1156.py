# Generated by Django 3.0.6 on 2020-05-12 11:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20200512_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('year', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('semester', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('price', models.IntegerField(default=0)),
                ('sold', models.BooleanField(default=False)),
                ('contains_books', models.BooleanField(default=False)),
                ('contains_notes', models.BooleanField(default=False)),
                ('contains_readings', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_bookset', to='registrations.Course')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='bookset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='set_books', to='registrations.BookSet'),
        ),
        migrations.AlterField(
            model_name='book',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_books', to='registrations.Course'),
        ),
    ]
