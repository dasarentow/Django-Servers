# Generated by Django 4.2.1 on 2023-05-11 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0036_alter_topic_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2023, 5, 11, 14, 10, 32, 160376)),
        ),
    ]
