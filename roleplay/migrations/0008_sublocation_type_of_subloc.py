# Generated by Django 3.0.5 on 2021-03-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('roleplay', '0007_auto_20210309_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='sublocation',
            name='type_of_subloc',
            field=models.CharField(
                choices=[('none', 'Подлокация'), ('trader', 'Лавка торговца'), ('mechanic', 'Рабочее место механика'),
                         ('bar', 'Бар'), ('medic', 'Медпункт'), ('abandoned', 'Заброшка')], default='none',
                max_length=100, verbose_name='Тип подлокации'),
        ),
    ]