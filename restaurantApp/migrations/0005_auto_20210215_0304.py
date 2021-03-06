# Generated by Django 3.1.6 on 2021-02-15 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0004_auto_20210215_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='mealDescription',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='menu',
            name='mealName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
