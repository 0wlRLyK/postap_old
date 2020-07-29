# Generated by Django 3.0.5 on 2020-07-29 15:13

import ckeditor_uploader.fields
import django.core.validators
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('entries', '0022_delete_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entryarticle',
            old_name='atMain',
            new_name='at_main',
        ),
        migrations.RenameField(
            model_name='entryarticle',
            old_name='inTop',
            new_name='in_top',
        ),
        migrations.RenameField(
            model_name='entryarticle',
            old_name='shortDescript',
            new_name='short_descript',
        ),
        migrations.RenameField(
            model_name='entryfaq',
            old_name='questionDescript',
            new_name='question_descript',
        ),
        migrations.RenameField(
            model_name='entryfile',
            old_name='atMain',
            new_name='at_main',
        ),
        migrations.RenameField(
            model_name='entryfile',
            old_name='inTop',
            new_name='in_top',
        ),
        migrations.RenameField(
            model_name='entryfile',
            old_name='shortDescript',
            new_name='short_descript',
        ),
        migrations.RenameField(
            model_name='entryimagegallery',
            old_name='atMain',
            new_name='at_main',
        ),
        migrations.RenameField(
            model_name='entryimagegallery',
            old_name='inTop',
            new_name='in_top',
        ),
        migrations.RenameField(
            model_name='entryimagegallery',
            old_name='shortDescript',
            new_name='short_descript',
        ),
        migrations.RenameField(
            model_name='entrynews',
            old_name='atMain',
            new_name='at_main',
        ),
        migrations.RenameField(
            model_name='entrynews',
            old_name='inTop',
            new_name='in_top',
        ),
        migrations.RenameField(
            model_name='entrynews',
            old_name='shortDescript',
            new_name='short_descript',
        ),
        migrations.AddField(
            model_name='entryarticle',
            name='posted',
            field=models.BooleanField(default=True, verbose_name='Материал опубликован'),
        ),
        migrations.AddField(
            model_name='entryfile',
            name='posted',
            field=models.BooleanField(default=True, verbose_name='Материал опубликован'),
        ),
        migrations.AddField(
            model_name='entryimagegallery',
            name='posted',
            field=models.BooleanField(default=True, verbose_name='Материал опубликован'),
        ),
        migrations.AddField(
            model_name='entrynews',
            name='posted',
            field=models.BooleanField(default=True, verbose_name='Материал опубликован'),
        ),
        migrations.AddField(
            model_name='games',
            name='release_date',
            field=models.DateField(blank=True, default='2010-01-01', verbose_name='Дата релиза'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoriesarticle',
            name='icon',
            field=models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                   upload_to='entries/categories',
                                   validators=[django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                   verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='categoriesfaq',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='categoriesfaq',
            name='icon',
            field=models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                   upload_to='entries/categories',
                                   validators=[django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                   verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='categoriesfaq',
            name='image',
            field=stdimage.models.StdImageField(blank=True, default='postap.png', upload_to='entries',
                                                verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='categoriesfaq',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='categoriesfaq',
            name='slug',
            field=models.CharField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='categoriesfiles',
            name='icon',
            field=models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                   upload_to='entries/categories',
                                   validators=[django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                   verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='categoriesimages',
            name='icon',
            field=models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                   upload_to='entries/categories',
                                   validators=[django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                   verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='categoriesmods',
            name='icon',
            field=models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                   upload_to='entries/categories',
                                   validators=[django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                   verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='categoriesnews',
            name='icon',
            field=models.FileField(blank=True, default='postap.png', help_text='Форматы svg, png, gif',
                                   upload_to='entries/categories',
                                   validators=[django.core.validators.FileExtensionValidator(['png', 'gif', 'svg'])],
                                   verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='entryarticle',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала'),
        ),
        migrations.AlterField(
            model_name='entryfile',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала'),
        ),
        migrations.AlterField(
            model_name='entryimagegallery',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='slug',
            field=models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='entrynews',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время добавления материала'),
        ),
        migrations.AlterField(
            model_name='games',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='games',
            name='slug',
            field=models.SlugField(help_text='Навзание, которое будет отображаться в URL', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='games',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
