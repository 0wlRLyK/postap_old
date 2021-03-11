# Generated by Django 3.0.5 on 2021-02-16 21:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0008_auto_20210216_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1),
                                                                          django.core.validators.MaxValueValidator(5)],
                                                   verbose_name='Rank of hero'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='rpl_rank',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1),
                                                                          django.core.validators.MaxValueValidator(10)],
                                                   verbose_name='Rank of user'),
        ),
    ]