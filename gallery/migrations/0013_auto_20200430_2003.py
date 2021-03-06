# Generated by Django 3.0.5 on 2020-04-30 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0012_remove_gallery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='galleryitem',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image',
                                    to='gallery.Gallery'),
        ),
        migrations.DeleteModel(
            name='TEST',
        ),
    ]
