# Generated by Django 3.0.5 on 2020-05-03 21:21

import django.core.validators
import django.db.models.deletion
import entries.models
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0014_auto_20200503_1455'),
        ('entries', '0004_categoriesfiles_entryfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='Название игры')),
                ('slug', models.SlugField(help_text='Навзание, которое будет отображаться в URL', unique=True)),
                ('bg', models.ImageField(upload_to=entries.models.upload_to_games, verbose_name='Фоновое изображение')),
                ('image', models.ImageField(upload_to=entries.models.upload_to_games, verbose_name='Обложка игры')),
                ('logo', models.FileField(blank=True, help_text='Форматы svg, png, gif', upload_to='entries/categories',
                                          validators=[
                                              django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Логотип игры')),
                ('descript', tinymce.models.HTMLField()),
                ('features', tinymce.models.HTMLField(blank=True)),
                ('requirements', tinymce.models.HTMLField(blank=True)),
                ('objgallery',
                 models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gallery.Gallery')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]
