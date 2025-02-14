# Generated by Django 5.1.6 on 2025-02-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('condition', models.CharField(max_length=100)),
                ('humidity', models.PositiveIntegerField()),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
