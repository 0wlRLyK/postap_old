# Generated by Django 3.0.5 on 2021-03-04 22:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('roleplay', '0003_mechanic_npcminigame'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='x_coord',
            field=models.SmallIntegerField(default=0, help_text='Расположение элемента по X координате',
                                           verbose_name='X координата'),
        ),
        migrations.AddField(
            model_name='area',
            name='y_coord',
            field=models.SmallIntegerField(default=0, help_text='Расположение элемента по Y координате',
                                           verbose_name='Y координата'),
        ),
        migrations.AddField(
            model_name='location',
            name='map',
            field=models.ImageField(default='postap.png', upload_to='roleplay/location/maps/'),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='coef_repair',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.2),
                                                           django.core.validators.MaxValueValidator(5)],
                                    verbose_name='Коєфициент починки'),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='inf',
            field=models.BooleanField(default=False, verbose_name='Бесконечны ли деньги'),
        ),
        migrations.AlterField(
            model_name='npcminigame',
            name='inf',
            field=models.BooleanField(default=False, verbose_name='Бесконечны ли деньги'),
        ),
        migrations.AlterField(
            model_name='trader',
            name='inf',
            field=models.BooleanField(default=False, verbose_name='Бесконечны ли деньги'),
        ),
    ]
