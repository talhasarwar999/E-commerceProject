# Generated by Django 3.2.4 on 2022-01-08 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='media/box/icon')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sold_Times',
            new_name='sold_times',
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='sub_attribute',
        ),
        migrations.RemoveField(
            model_name='couponcode',
            name='product',
        ),
        migrations.RemoveField(
            model_name='couponcode',
            name='type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_Active',
        ),
        migrations.AddField(
            model_name='attribute',
            name='grand_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.grandcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grandcategory',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_attribute',
            field=models.ManyToManyField(blank=True, related_name='sub_property', to='product.SubAttribute'),
        ),
        migrations.AlterField(
            model_name='grandcategory',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='child_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.childcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='grand_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.grandcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.parentcategory'),
        ),
        migrations.CreateModel(
            name='SAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.attribute')),
                ('product', models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='box',
            field=models.ManyToManyField(blank=True, to='product.Box'),
        ),
        migrations.AddField(
            model_name='productsliderimage',
            name='related_sub_attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_sub_attribute', to='product.sattribute'),
        ),
        migrations.AlterField(
            model_name='productsliderimage',
            name='sub_attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.sattribute'),
        ),
    ]
