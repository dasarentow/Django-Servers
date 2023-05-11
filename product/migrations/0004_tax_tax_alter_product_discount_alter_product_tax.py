# Generated by Django 4.1.5 on 2023-02-23 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_cart_discount_tax_cartitem_product_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax',
            name='tax',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.tax'),
        ),
    ]