# Generated by Django 4.1.5 on 2023-03-09 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_cartitem_quantity'),
        ('order', '0011_remove_order_price_remove_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='product.cartitem'),
        ),
    ]
