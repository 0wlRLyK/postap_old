# Generated by Django 2.0.7 on 2018-07-06 18:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DialogMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('first',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_thread_first',
                                   to=settings.AUTH_USER_MODEL)),
                ('second',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_thread_second',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dialogmessage',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='chat.Thread'),
        ),
        migrations.AddField(
            model_name='dialogmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='sender'),
        ),
    ]
