# Generated by Django 4.0.2 on 2022-02-22 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.FileField(default=None, null=True, upload_to='category/')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('type_disc', models.CharField(choices=[('PRI', 'price'), ('PER', 'percent')], max_length=7)),
                ('value', models.IntegerField()),
            ],
            options={
                'verbose_name': 'discount',
                'verbose_name_plural': 'discounts',
            },
        ),
        migrations.CreateModel(
            name='OffCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('type_disc', models.CharField(choices=[('PRI', 'price'), ('PER', 'percent')], max_length=7)),
                ('value', models.IntegerField()),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'off code',
                'verbose_name_plural': 'off codes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(default=None, null=True, upload_to='product/')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.discount')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
