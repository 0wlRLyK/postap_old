# Generated by Django 3.0.5 on 2020-05-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0016_auto_20200526_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofiles',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique=True, verbose_name='Слаг'),
        ),
    ]