# Generated by Django 5.0.1 on 2024-05-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreverfinds', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]