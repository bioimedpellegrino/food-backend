# Generated by Django 3.0 on 2023-03-14 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20230314_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_calories',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_carbs',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_cholestorol',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_fiber',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_protein',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_saturatedfat',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_sodium',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_sugars',
        ),
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='substitute_totalfat',
        ),
    ]