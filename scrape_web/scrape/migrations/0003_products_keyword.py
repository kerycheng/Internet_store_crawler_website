# Generated by Django 4.1.5 on 2023-01-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0002_products_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='keyword',
            field=models.TextField(default='Keyword'),
        ),
    ]