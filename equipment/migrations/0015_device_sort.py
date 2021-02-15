# Generated by Django 3.0.5 on 2021-02-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equipment', '0014_auto_20210107_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='sort',
            field=models.CharField(
                choices=[('pda', 'PDA'), ('light', 'Фонарик/ПНВ'), ('detector', 'Детектор'), ('binocular', 'Бинокль'),
                         ('device', 'Прочее')], default='device', max_length=100, verbose_name='Тип устройства'),
        ),
    ]
