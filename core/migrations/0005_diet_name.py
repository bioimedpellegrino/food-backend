# Generated by Django 3.0 on 2023-02-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230211_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
