# Generated by Django 4.1.5 on 2023-02-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_stripe_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
