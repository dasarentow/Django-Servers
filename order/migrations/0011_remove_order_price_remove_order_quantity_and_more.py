# Generated by Django 4.1.5 on 2023-03-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_remove_order_products_remove_orderitem_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(blank=True, max_length=30000, null=True),
        ),
    ]