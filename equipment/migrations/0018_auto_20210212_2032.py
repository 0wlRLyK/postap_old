# Generated by Django 3.0.5 on 2021-02-12 18:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('equipment', '0017_auto_20210203_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backpack',
            old_name='carry_weight',
            new_name='weight',
        ),
    ]
