# Generated by Django 3.0.5 on 2020-04-25 18:41

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('entries', '0014_auto_20200425_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='objID',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='objID',
        ),
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
