# Generated by Django 3.0.5 on 2020-04-26 13:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0002_auto_20200426_1605'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gallerieditem',
            unique_together={('image', 'gallery')},
        ),
        migrations.AlterIndexTogether(
            name='gallerieditem',
            index_together={('image',)},
        ),
        migrations.RemoveField(
            model_name='gallerieditem',
            name='object_id',
        ),
    ]
