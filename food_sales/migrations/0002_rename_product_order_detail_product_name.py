# Generated by Django 4.1.5 on 2023-01-06 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_detail',
            old_name='product',
            new_name='product_name',
        ),
    ]