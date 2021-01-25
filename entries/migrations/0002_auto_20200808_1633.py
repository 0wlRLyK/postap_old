# Generated by Django 3.0.5 on 2020-08-08 13:33

import ckeditor_uploader.fields
import django.core.validators
import entries.models
import hitcount.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug',
                 models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('publ_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала')),
                ('short_descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание')),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(default='postap.png', null=True,
                                                        upload_to=entries.models.upload_to_entries,
                                                        verbose_name='Илюстрация')),
                ('in_top', models.BooleanField(blank='True', default=False, verbose_name='Закрепить материал')),
                ('at_main',
                 models.BooleanField(blank='True', default=False, verbose_name='Вывести материал на главную страницу')),
                ('posted', models.BooleanField(default=True, verbose_name='Материал опубликован')),
                ('source', models.URLField(blank=True, verbose_name='Источник')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
            bases=(hitcount.models.HitCountMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                          upload_to='entries/categories', validators=[
                        django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория статей',
                'verbose_name_plural': 'Категории статей',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя автора')),
                ('slug', models.SlugField(help_text='Навзание, которое будет отображаться в URL', unique=True)),
                ('nickname', models.CharField(max_length=200, verbose_name='Никнейм автора')),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField()),
                ('domain', models.CharField(
                    choices=[('youtuber', 'Видео блогер'), ('bloger', 'Блогер'), ('moder', 'Мододел'),
                             ('musician', 'Музыкант'), ('painter', 'Художник'), ('artist', 'Творец'),
                             ('writer', 'Писатель'), ('unique_person', 'Уникальная персона')], max_length=200,
                    verbose_name='Сфера деятельности')),
                ('avatar', stdimage.models.StdImageField(upload_to=entries.models.upload_to_authors,
                                                         verbose_name='Аватар автора')),
                ('bg', stdimage.models.StdImageField(upload_to=entries.models.upload_to_authors,
                                                     verbose_name='Аватар автора')),
                ('vk', models.URLField(blank=True)),
                ('discord', models.URLField(blank=True)),
                ('tg', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('twitch', models.URLField(blank=True)),
                ('artstation', models.URLField(blank=True)),
                ('devianart', models.URLField(blank=True)),
                ('site', models.URLField(blank=True)),
                ('other1', models.URLField(blank=True)),
                ('other2', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, verbose_name='Вопрос')),
                ('publ_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('question_descript',
                 ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание вопроса')),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание ответа')),
                ('posted', models.BooleanField(default=True, verbose_name='Материал опубликован')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='FaqCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                          upload_to='entries/categories', validators=[
                        django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория FAQ',
                'verbose_name_plural': 'Категории FAQ',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug',
                 models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('publ_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала')),
                ('short_descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание')),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(default='postap.png', null=True,
                                                        upload_to=entries.models.upload_to_entries,
                                                        verbose_name='Илюстрация')),
                ('in_top', models.BooleanField(blank='True', default=False, verbose_name='Закрепить материал')),
                ('at_main',
                 models.BooleanField(blank='True', default=False, verbose_name='Вывести материал на главную страницу')),
                ('posted', models.BooleanField(default=True, verbose_name='Материал опубликован')),
                ('file', models.FileField(blank=True, upload_to=entries.models.upload_to_file, verbose_name='Файл')),
                ('torrent1', models.FileField(blank=True, upload_to=entries.models.upload_to_torrent,
                                              validators=[django.core.validators.FileExtensionValidator(['torrent'])],
                                              verbose_name='Торрент #1')),
                ('torrent2', models.FileField(blank=True, upload_to=entries.models.upload_to_torrent,
                                              validators=[django.core.validators.FileExtensionValidator(['torrent'])],
                                              verbose_name='Торрент #1')),
                ('torrent3', models.FileField(blank=True, upload_to=entries.models.upload_to_torrent,
                                              validators=[django.core.validators.FileExtensionValidator(['torrent'])],
                                              verbose_name='Торрент #1')),
                ('gdrive', models.URLField(blank=True, verbose_name='Google')),
                ('yadrive', models.URLField(blank=True, verbose_name='Yandex')),
                ('mega', models.URLField(blank=True, verbose_name='MEGA')),
                ('source1', models.URLField(blank=True, verbose_name='Другой источник #1')),
                ('source2', models.URLField(blank=True, verbose_name='Другой источник #2')),
                ('source3', models.URLField(blank=True, verbose_name='Другой источник #3')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
            bases=(hitcount.models.HitCountMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FileCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                          upload_to='entries/categories', validators=[
                        django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория файлов',
                'verbose_name_plural': 'Категории файлов',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug',
                 models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('bg', models.ImageField(upload_to=entries.models.upload_to_games, verbose_name='Фоновое изображение')),
                ('image',
                 stdimage.models.StdImageField(upload_to=entries.models.upload_to_games, verbose_name='Обложка игры')),
                ('logo', models.FileField(blank=True, help_text='Форматы svg, png, gif',
                                          upload_to=entries.models.upload_to_games, validators=[
                        django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Логотип игры')),
                ('release_date', models.DateField(blank=True, verbose_name='Дата релиза')),
                ('features', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('requirements', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Навзание квеста')),
                ('type0f', models.CharField(
                    choices=[('main', 'Сюжетный квест'), ('side', 'Побочный квест'), ('additional', 'Дополнительный'),
                             ('items', 'Метонахождение квестовых предметов'), ('tools', 'Метонахождение инстурментов'),
                             ('interesting', 'Интересности'), ('easter_eggs', 'Пасхалки'), ('other', 'Другое')],
                    max_length=100, verbose_name='Тип гайда')),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание квеста')),
                ('solution', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Решение квеста')),
            ],
            options={
                'verbose_name': 'Гайд по прохождению',
                'verbose_name_plural': 'Гайды по прохождению',
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug',
                 models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('publ_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала')),
                ('short_descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание')),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(default='postap.png', null=True,
                                                        upload_to=entries.models.upload_to_entries,
                                                        verbose_name='Илюстрация')),
                ('in_top', models.BooleanField(blank='True', default=False, verbose_name='Закрепить материал')),
                ('at_main',
                 models.BooleanField(blank='True', default=False, verbose_name='Вывести материал на главную страницу')),
                ('posted', models.BooleanField(default=True, verbose_name='Материал опубликован')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
            bases=(hitcount.models.HitCountMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ImageGalleryCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                          upload_to='entries/categories', validators=[
                        django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория галереи',
                'verbose_name_plural': 'Категории галереи',
            },
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug',
                 models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('plot', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Коротко о сюжете')),
                ('features', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Особенности')),
                ('innovations',
                 ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Нововведения')),
                ('gameplay', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Гемйплей')),
                ('locations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Локации')),
                ('weapons', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Другое')),
                ('other', ckeditor_uploader.fields.RichTextUploadingField(blank=True,
                                                                          verbose_name='Другие особенности и нововведения модификации')),
            ],
            options={
                'verbose_name': 'Мод',
                'verbose_name_plural': 'Моды',
            },
            bases=(hitcount.models.HitCountMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ModCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                          upload_to='entries/categories', validators=[
                        django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория модов',
                'verbose_name_plural': 'Категории модов',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug',
                 models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('publ_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала')),
                ('short_descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание')),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(default='postap.png', null=True,
                                                        upload_to=entries.models.upload_to_entries,
                                                        verbose_name='Илюстрация')),
                ('in_top', models.BooleanField(blank='True', default=False, verbose_name='Закрепить материал')),
                ('at_main',
                 models.BooleanField(blank='True', default=False, verbose_name='Вывести материал на главную страницу')),
                ('posted', models.BooleanField(default=True, verbose_name='Материал опубликован')),
                ('source', models.URLField(blank=True, verbose_name='Источник')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
            bases=(hitcount.models.HitCountMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug',
                 models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True)),
                ('descript', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                        verbose_name='Изображение')),
                ('icon', models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                          upload_to='entries/categories', validators=[
                        django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                          verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория новостей',
                'verbose_name_plural': 'Категории новостей',
            },
        ),
        migrations.RemoveField(
            model_name='categoriesarticle',
            name='categories_ptr',
        ),
        migrations.RemoveField(
            model_name='categoriesnews',
            name='categories_ptr',
        ),
        migrations.RemoveField(
            model_name='entryarticle',
            name='author',
        ),
        migrations.RemoveField(
            model_name='entryarticle',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='entryarticle',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='entryarticle',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='entrynews',
            name='author',
        ),
        migrations.RemoveField(
            model_name='entrynews',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='entrynews',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='entrynews',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='CategoriesArticle',
        ),
        migrations.DeleteModel(
            name='CategoriesNews',
        ),
        migrations.DeleteModel(
            name='EntryArticle',
        ),
        migrations.DeleteModel(
            name='EntryNews',
        ),
    ]