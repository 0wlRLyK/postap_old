# Generated by Django 3.0.5 on 2020-04-23 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('entries', '0004_auto_20200423_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesArticles',
            fields=[
                ('categories_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='entries.Categories')),
            ],
            options={
                'verbose_name': 'Категория cтатей',
                'verbose_name_plural': 'Категории статей',
            },
            bases=('entries.categories',),
        ),
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
    ]
