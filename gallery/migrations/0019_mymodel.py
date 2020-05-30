# Generated by Django 3.0.5 on 2020-05-28 18:21

import image_cropping.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0018_auto_20200515_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', image_cropping.fields.ImageCropField(blank=True, upload_to='uploaded_images')),
                ('cropping',
                 image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False,
                                                       free_crop=False, help_text=None, hide_image_field=False,
                                                       size_warning=False, verbose_name='cropping')),
            ],
        ),
    ]
