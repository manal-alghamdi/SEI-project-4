# Generated by Django 3.1.6 on 2021-02-14 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0002_auto_20210214_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealPicture', models.TextField()),
                ('mealName', models.CharField(max_length=50)),
                ('mealDescription', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('Appetizers', 'Appetizers'), ('Snacks', 'Snacks'), ('Soups & Salads', 'Soups & Salads'), ('Pizzas', 'Pizzas'), ('Sandwiches', 'Sandwiches'), ('Steaks & Seafood', 'Steaks & Seafood'), ('Desserts', 'Desserts'), ('Drinks', 'Drinks')], default='All', max_length=20)),
                ('calories', models.PositiveSmallIntegerField(null=True)),
                ('price', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
    ]