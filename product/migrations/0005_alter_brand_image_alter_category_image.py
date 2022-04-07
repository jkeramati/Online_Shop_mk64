# Generated by Django 4.0.2 on 2022-03-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_category_image_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.FileField(blank=None, null=True, upload_to='brand/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='category/'),
        ),
    ]