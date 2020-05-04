# Generated by Django 3.0.5 on 2020-05-03 21:53

import entries.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('entries', '0005_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='objgallery',
        ),
        migrations.AlterField(
            model_name='games',
            name='image',
            field=stdimage.models.StdImageField(upload_to=entries.models.upload_to_games, verbose_name='Обложка игры'),
        ),
    ]
