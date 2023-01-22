# Generated by Django 3.0 on 2023-01-22 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_food_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
        migrations.CreateModel(
            name='FoodSubstitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('lasagne', 'Lasagne'), ('lattuga', 'Lattuga'), ('formaggio', 'Formaggio'), ('pizza', 'Pizza'), ('carne', 'Carne'), ('pesce', 'Pesce')], default='lattuga', max_length=256)),
                ('quantity', models.DecimalField(decimal_places=2, default=100.0, max_digits=7)),
                ('calories', models.IntegerField(default=0)),
                ('totalfat', models.IntegerField(default=0)),
                ('saturatedfat', models.IntegerField(default=0)),
                ('carbs', models.IntegerField(default=0)),
                ('cholestorol', models.IntegerField(default=0)),
                ('sodium', models.IntegerField(default=0)),
                ('fiber', models.IntegerField(default=0)),
                ('sugars', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Food')),
            ],
            options={
                'verbose_name': 'Food Substtute',
                'verbose_name_plural': 'Food Substtute',
            },
        ),
    ]