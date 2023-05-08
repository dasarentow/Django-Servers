# Generated by Django 4.1.5 on 2023-03-14 19:56

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0021_alter_topic_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='participants',
            field=models.ManyToManyField(related_name='all_participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2023, 3, 14, 19, 56, 38, 423993)),
        ),
    ]