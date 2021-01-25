# Generated by Django 3.0.5 on 2021-01-07 08:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0011_auto_20210103_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddonOutfit',
            fields=[
                ('item_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='equipment.Item')),
                ('sort', models.CharField(
                    choices=[('none', '/* NONE /*'), ('rookie', 'Одежда новичка'), ('cloak', 'Плащи'),
                             ('light', 'Легкая броня'), ('middle', 'Средняя броня'),
                             ('rhbz', 'Комбинезоны РХБЗ (радиоационной, химической и биологической защиты)'),
                             ('science_low', 'Научные комбинезоны(Низкий уровень)'),
                             ('science_high', 'Научные комбинезоны(Высокий уровень)'), ('seva', 'СЕВА'),
                             ('heavy', 'Тяжелая броня'), ('protoexo', 'Прототипы экзоскелета'), ('exo', 'Экзоскелеты'),
                             ('heavyexo', 'Тяжелые экзоскелеты')], max_length=100, verbose_name='Тип брони')),
                ('ballistic', models.FloatField(default=0, verbose_name='Балистическая защита уникального костюма')),
                ('burst', models.FloatField(default=0, verbose_name='Защита от разрыва уникального костюма')),
                ('kick', models.FloatField(default=0, verbose_name='Гашение удара уникального костюма')),
                ('explosion', models.FloatField(default=0, verbose_name='Защита от взрыва уникального костюма')),
                ('thermal', models.FloatField(default=0, verbose_name='Термозащита уникального костюма')),
                ('chemical', models.FloatField(default=0, verbose_name='Химащита уникального костюма')),
                ('electrical', models.FloatField(default=0, verbose_name='Электрозащита уникального костюма')),
                ('radioactive', models.FloatField(default=0, verbose_name='Радиоактивная уникального костюма')),
                ('psi', models.FloatField(default=0, verbose_name='Пси защита уникального костюма')),
                ('weight', models.FloatField(default=0, verbose_name='Переносимый вес уникального костюма')),
                ('arts_max', models.IntegerField(default=0, verbose_name='Колличество контейнеров для артефактов')),
                ('modules_max', models.IntegerField(default=0, verbose_name='Колличество контейнеров для модулей')),
                ('running', models.BooleanField(default=True, verbose_name='Возможность бега')),
                ('accuracy', models.FloatField(default=0, verbose_name='Точность')),
                ('damage', models.FloatField(default=0, verbose_name='Повреждение')),
                ('convenience', models.FloatField(default=0, verbose_name='Удобность')),
                ('pace_of_fire', models.FloatField(default=0, verbose_name='Скорострельность')),
                ('capacity', models.IntegerField(default=0, verbose_name='Ёмкость')),
            ],
            options={
                'verbose_name': 'Аддон',
                'verbose_name_plural': 'Аддоны',
            },
            bases=('equipment.item', models.Model),
        ),
        migrations.RemoveField(
            model_name='equip',
            name='armor',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='backpack',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='belt1',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='belt2',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='belt3',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='belt4',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='belt5',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='belt6',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='container1',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='container2',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='container3',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='container4',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='container5',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='container6',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='device1',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='device2',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='device3',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='helmet',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='slot1',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='slot2',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='slot3',
        ),
        migrations.AddField(
            model_name='equipitem',
            name='profile',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='item_profile', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Профиль пользователя'),
        ),
    ]