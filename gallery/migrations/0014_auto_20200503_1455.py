# Generated by Django 3.0.5 on 2020-05-03 11:55

import gallery.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0013_auto_20200430_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='image',
            field=stdimage.models.StdImageField(upload_to=gallery.models.upload_to),
        ),
    ]
