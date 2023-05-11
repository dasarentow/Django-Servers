# Generated by Django 4.1.5 on 2023-03-09 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0014_remove_cartitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL),
        ),
    ]
