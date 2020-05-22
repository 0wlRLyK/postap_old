# Generated by Django 3.0.5 on 2020-05-21 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cities_light', '0010_auto_20200508_1851'),
        ('users', '0006_auto_20200522_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofiles',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='cities_light.City'),
        ),
        migrations.AlterField(
            model_name='usersprofiles',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='cities_light.Country'),
        ),
    ]
