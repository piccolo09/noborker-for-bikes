# Generated by Django 4.2 on 2023-04-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bike_info', '0002_delete_vehiclecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Vehicle Cateogry Name')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Bike Categories',
            },
        ),
    ]
