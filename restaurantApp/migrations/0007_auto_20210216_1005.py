# Generated by Django 3.1.6 on 2021-02-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0006_auto_20210215_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='typeoftable',
            field=models.CharField(choices=[('Table of 5 table', 'TABLE OF 5 TABLE'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], max_length=50, null=True),
        ),
    ]
