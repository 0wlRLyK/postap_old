# Generated by Django 3.0.5 on 2020-07-29 20:28

import gallery.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0020_delete_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=gallery.models.upload_to),
        ),
    ]