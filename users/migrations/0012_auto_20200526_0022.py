# Generated by Django 3.0.5 on 2020-05-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0011_auto_20200524_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersprofiles',
            name='hp',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Health points'),
        ),
        migrations.AddField(
            model_name='usersprofiles',
            name='rad',
            field=models.SmallIntegerField(default=0, verbose_name='Radiation points'),
        ),
        migrations.AddField(
            model_name='usersprofiles',
            name='satiety',
            field=models.SmallIntegerField(default=20, verbose_name='Satiety points'),
        ),
        migrations.AlterField(
            model_name='usersprofiles',
            name='city',
            field=models.CharField(blank=True, default=' ', max_length=50, verbose_name='City'),
        ),
    ]