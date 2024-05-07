# Generated by Django 5.0.1 on 2024-06-23 12:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreverfinds', '0004_dinningproduct_orderitem_dining_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='dining_product',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='default-slug'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='default-title', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='foreverfinds.category'),
        ),
        migrations.DeleteModel(
            name='DinningProduct',
        ),
    ]
