# Generated by Django 3.0.5 on 2020-05-27 21:28

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0019_auto_20200527_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofiles',
            name='mugshot_full',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_to_mugshot,
                                    verbose_name='Full avatar'),
        ),
    ]