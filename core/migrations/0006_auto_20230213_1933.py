# Generated by Django 3.0 on 2023-02-13 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_diet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Patient'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Patient'),
        ),
    ]