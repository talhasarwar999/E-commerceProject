# Generated by Django 3.2.4 on 2022-01-08 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220108_1324'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='sub_attributes',
            field=models.ManyToManyField(blank=True, to='product.SubAttribute'),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.couponcode'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
