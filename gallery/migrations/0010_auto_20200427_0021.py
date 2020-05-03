# Generated by Django 3.0.5 on 2020-04-26 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0009_auto_20200427_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='entry',
        ),
        migrations.AddField(
            model_name='test',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery'),
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='test')),
                ('entry',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery')),
            ],
        ),
    ]
