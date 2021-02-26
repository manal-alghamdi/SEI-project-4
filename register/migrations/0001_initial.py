# Generated by Django 3.1.6 on 2021-02-13 17:44

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
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeoftable', models.CharField(max_length=50, null=True)),
                ('purpose', models.CharField(max_length=50, null=True)),
                ('mealplan', models.CharField(max_length=40, null=True)),
                ('arrivaltime', models.TimeField(null=True)),
                ('bookdate', models.CharField(max_length=40, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nreservation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]