# Generated by Django 4.1.5 on 2023-01-12 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
