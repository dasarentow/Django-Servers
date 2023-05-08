# Generated by Django 4.1.5 on 2023-03-13 17:24

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0008_alter_topic_updated'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='Responses',
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2023, 3, 13, 17, 24, 43, 455331)),
        ),
    ]