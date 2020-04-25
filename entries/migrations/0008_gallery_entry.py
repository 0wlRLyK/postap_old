# Generated by Django 3.0.5 on 2020-04-23 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('entries', '0007_remove_gallery_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='contenttypes.ContentType'),
        ),
    ]
