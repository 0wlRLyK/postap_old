# Generated by Django 3.0.5 on 2020-05-25 22:15

import datetime

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0013_usersprofiles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofiles',
            name='birthday',
            field=models.DateField(default=datetime.date(1990, 1, 6), verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='usersprofiles',
            name='signature',
            field=ckeditor.fields.RichTextField(blank=True, default='', verbose_name='Signature'),
        ),
        migrations.AlterField(
            model_name='usersprofiles',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True, verbose_name='Слаг'),
        ),
    ]