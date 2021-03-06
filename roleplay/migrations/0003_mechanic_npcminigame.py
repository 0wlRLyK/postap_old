# Generated by Django 3.0.5 on 2021-02-25 18:24

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
import roleplay.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0009_auto_20210216_2332'),
        ('equipment', '0019_auto_20210225_2024'),
        ('roleplay', '0002_auto_20210216_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPCMinigame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('full_name', models.CharField(max_length=150, verbose_name='Полное Имя')),
                ('bio', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
                ('rank', models.PositiveSmallIntegerField(default=1,
                                                          validators=[django.core.validators.MinValueValidator(1),
                                                                      django.core.validators.MaxValueValidator(10)],
                                                          verbose_name='Ранг')),
                ('avatar',
                 models.ImageField(default='img/profile/no_data.gif', upload_to=roleplay.models.npc_upload_to_ava,
                                   verbose_name='Аватар')),
                ('image', models.ImageField(help_text='(Желательно в полный рост и по центру)',
                                            upload_to=roleplay.models.npc_upload_to_img,
                                            verbose_name='Изображение персонажа')),
                ('money', models.IntegerField(default=0, verbose_name='Деньги')),
                ('inf', models.BooleanField(default=True, verbose_name='Бесконечны ли деньги')),
                ('spec', models.CharField(
                    choices=[('trader', 'Торговец'), ('mechanic', 'Механик'), ('medic', 'Медик'), ('barmen', 'Бармен'),
                             ('npc', 'Сталкер')], default='npc', max_length=25, verbose_name='Специальность')),
                ('coef_trade', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.2),
                                                                        django.core.validators.MaxValueValidator(5)],
                                                 verbose_name='Коєфициент продажи')),
                ('coef_buy', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.2),
                                                                      django.core.validators.MaxValueValidator(5)],
                                               verbose_name='Коєфициент покупки')),
                ('faction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                              related_name='rp_npc_minigame', to='users.Faction',
                                              verbose_name='Группировка')),
                ('items', models.ManyToManyField(blank=True, to='equipment.Item', verbose_name='Предметы на продажу')),
                ('sublocation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                                  to='roleplay.SubLocation', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'NPC с миниигрой',
                'verbose_name_plural': 'NPC`s с миниигрой',
            },
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('full_name', models.CharField(max_length=150, verbose_name='Полное Имя')),
                ('bio', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
                ('rank', models.PositiveSmallIntegerField(default=1,
                                                          validators=[django.core.validators.MinValueValidator(1),
                                                                      django.core.validators.MaxValueValidator(10)],
                                                          verbose_name='Ранг')),
                ('avatar',
                 models.ImageField(default='img/profile/no_data.gif', upload_to=roleplay.models.npc_upload_to_ava,
                                   verbose_name='Аватар')),
                ('image', models.ImageField(help_text='(Желательно в полный рост и по центру)',
                                            upload_to=roleplay.models.npc_upload_to_img,
                                            verbose_name='Изображение персонажа')),
                ('money', models.IntegerField(default=0, verbose_name='Деньги')),
                ('inf', models.BooleanField(default=True, verbose_name='Бесконечны ли деньги')),
                ('coef_trade', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.2),
                                                                        django.core.validators.MaxValueValidator(5)],
                                                 verbose_name='Коєфициент продажи')),
                ('coef_buy', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.2),
                                                                      django.core.validators.MaxValueValidator(5)],
                                               verbose_name='Коєфициент покупки')),
                ('coef_repair', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.2),
                                                                         django.core.validators.MaxValueValidator(5)],
                                                  verbose_name='Коєфициент покупки')),
                ('faction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                              related_name='rp_npc_mechanic', to='users.Faction',
                                              verbose_name='Группировка')),
                ('items', models.ManyToManyField(blank=True, to='equipment.Item', verbose_name='Предметы на продажу')),
                ('sublocation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                                  to='roleplay.SubLocation', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Механик',
                'verbose_name_plural': 'Механики',
            },
        ),
    ]
