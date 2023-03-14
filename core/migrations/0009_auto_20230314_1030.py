# Generated by Django 3.0 on 2023-03-14 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_food_kjoules'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodsubstitute',
            name='food',
        ),
        migrations.AddField(
            model_name='foodsubstitute',
            name='food_substitute',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='food_substitute', to='core.Food'),
        ),
        migrations.AddField(
            model_name='foodsubstitute',
            name='food_to_substitute',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='food_to_substitute', to='core.Food'),
        ),
    ]
