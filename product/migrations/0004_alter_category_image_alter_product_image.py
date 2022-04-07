# Generated by Django 4.0.2 on 2022-03-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_brand_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='product/'),
        ),
    ]