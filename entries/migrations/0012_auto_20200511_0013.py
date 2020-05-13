# Generated by Django 3.0.5 on 2020-05-10 21:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('entries', '0011_auto_20200510_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='categories',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='entryarticle',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='entryarticle',
            name='shortDescript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='entryfile',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='entryfile',
            name='shortDescript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='entryguide',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание квеста'),
        ),
        migrations.AlterField(
            model_name='entryguide',
            name='solution',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Решение квеста'),
        ),
        migrations.AlterField(
            model_name='entryimagegallery',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='entryimagegallery',
            name='shortDescript',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='features',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Особенности'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='gameplay',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Гемйплей'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='innovations',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Нововведения'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='locations',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Локации'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='other',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True,
                                                                  verbose_name='Другие особенности и нововведения модификации'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='plot',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Коротко о сюжете'),
        ),
        migrations.AlterField(
            model_name='entrymod',
            name='weapons',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Другое'),
        ),
        migrations.AlterField(
            model_name='games',
            name='descript',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='games',
            name='features',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='games',
            name='requirements',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]