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

class Food(models.Model):
    name = models.CharField(max_length=256, choices=FOODS, default='lattuga')
    calories = models.IntegerField(default=0)
    totalfat = models.IntegerField(default=0)
    saturatedfat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    cholestorol = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    sugars = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

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
