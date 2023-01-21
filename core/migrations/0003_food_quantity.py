# Generated by Django 3.0 on 2023-01-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_foodlog_image_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=7),
        ),
    ]