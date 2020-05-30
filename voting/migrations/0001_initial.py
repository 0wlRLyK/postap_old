# Generated by Django 3.0.5 on 2020-05-15 22:19

import ckeditor_uploader.fields
import django.core.validators
import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('entries', '0022_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='voting/categories',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, help_text='Форматы svg, png, gif', upload_to='entries/categories',
                                          validators=[
                                              django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория голосований',
                'verbose_name_plural': 'Категории голосований',
            },
        ),
        migrations.CreateModel(
            name='VotingCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='voting/categories',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, help_text='Форматы svg, png, gif', upload_to='entries/categories',
                                          validators=[
                                              django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория голосований',
                'verbose_name_plural': 'Категории голосований',
            },
        ),
        migrations.CreateModel(
            name='ModVotingCategories',
            fields=[
                ('pollcategories_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='voting.PollCategories')),
            ],
            options={
                'verbose_name': 'Категория выборов модификаций',
                'verbose_name_plural': 'Категории выборов модификаций',
            },
            bases=('voting.pollcategories',),
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.VotingCategories',
                                   verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Голосование',
                'verbose_name_plural': 'Голосования',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_title', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.Voting')),
            ],
            options={
                'verbose_name': 'Вариант голосования',
                'verbose_name_plural': 'Варианты голосования',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.PollCategories',
                                   verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Голосование',
                'verbose_name_plural': 'Голосования',
            },
        ),
        migrations.CreateModel(
            name='ModVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.PollCategories',
                                   verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Голосование',
                'verbose_name_plural': 'Голосования',
            },
        ),
        migrations.CreateModel(
            name='ModChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('mod', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='entries.EntryMod')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.ModChoice')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.Poll')),
            ],
            options={
                'verbose_name': 'Вариант голосования',
                'verbose_name_plural': 'Варианты голосования',
            },
        ),
    ]