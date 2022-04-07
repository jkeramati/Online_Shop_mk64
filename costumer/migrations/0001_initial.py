# Generated by Django 4.0.2 on 2022-02-22 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('main_st', models.CharField(blank=True, max_length=30, null=True)),
                ('auxiliary_st', models.CharField(blank=True, max_length=30, null=True)),
                ('alley', models.CharField(blank=True, max_length=20, null=True)),
                ('No', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='costumer.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'costumer',
                'verbose_name_plural': 'costumers',
            },
        ),
    ]