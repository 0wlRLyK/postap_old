# Generated by Django 3.0.5 on 2020-04-26 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0003_auto_20200426_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='TEST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery')),
            ],
        ),
    ]
