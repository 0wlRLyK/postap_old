# Generated by Django 3.0.5 on 2021-02-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0007_auto_20210215_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='rpl_rank',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Rank of user'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Rank of hero'),
        ),
    ]
