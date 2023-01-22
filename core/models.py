from random import choices
from django.db import models

# Create your models here.

DAY_OF_WEEK = [("Lunedì","Lunedì"),
               ("Martedì", "Martedì"),
               ("Mercoledì", "Mercoledì"),
               ("Giovedì", "Giovedì"),
               ("Venerdì", "Venerdì"),
               ("Sabato", "Sabato"),
               ("Domenica", "Domenica"),
               ]

MEALS = [("Colazione", "Colazione"),
         ("Pranzo", "Pranzo"),
         ("Cena", "Cena"),
         ("Merenda", "Merenda"),
        ]

FOODS = [("lasagne", "Lasagne"),
         ("lattuga", "Lattuga"),
         ("formaggio", "Formaggio"),
         ("pizza", "Pizza"),
         ("carne", "Carne"),
         ("pesce", "Pesce"),
        ]

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    entry_date = models.DateField()

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weight'

    def __str__(self):
        return f'{self.user.username} - {self.weight} Kg in data {self.entry_date}'

class Food(models.Model):
    name = models.CharField(max_length=256, choices=FOODS, default='lattuga')
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00)
    calories = models.IntegerField(default=0)
    totalfat = models.IntegerField(default=0)
    saturatedfat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    cholestorol = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    sugars = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.user.username} - {self.food_consumed.food_name}'

class FoodSubstitute(models.Model):
    name = models.CharField(max_length=256, choices=FOODS, default='lattuga')
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00)
    calories = models.IntegerField(default=0)
    totalfat = models.IntegerField(default=0)
    saturatedfat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    cholestorol = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    sugars = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food Substtute'
        verbose_name_plural = 'Food Substtute'

class Image(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='get_images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.image}'

class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField()
    name = models.CharField(max_length=256, choices=MEALS, default='colazione')
    foods = models.ManyToManyField(Food)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.name}"

# Dieta insieme di pasti, ex: colazione, pranzo, cena, merenda
class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=DAY_OF_WEEK, default="Lunedì") 
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return f"{self.user} - {self.day_of_week}"       
