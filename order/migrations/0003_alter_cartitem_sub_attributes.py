# Generated by Django 3.2.4 on 2022-01-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220108_1324'),
        ('order', '0002_auto_20220108_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='sub_attributes',
            field=models.ManyToManyField(blank=True, to='product.SAttribute'),
        ),
    ]
