# Generated by Django 4.1.5 on 2023-03-11 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_topic_slug_alter_topic_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2023, 3, 11, 14, 56, 33, 754336)),
        ),
    ]
