from random import choices
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

DAY_OF_WEEK = [("lun", "Lunedì"),
               ("mar", "Martedì"),
               ("mer", "Mercoledì"),
               ("gio", "Giovedì"),
               ("ven", "Venerdì"),
               ("sab", "Sabato"),
               ("dom", "Domenica"),
               ("ven", "Lunedì-Venerdì"),
               ("all", "Tutti i giorni"),
               ]

MEALS = [("Colazione", "breakfast"),
         ("Pranzo", "launch"),
         ("Cena", "dinner"),
         ("Merenda", "snack"),
        ]

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256, blank=True, null=True)
    surname = models.CharField(max_length=256, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user,
            'name': self.name,
            'surname': self.surname,
            'birth_date': self.birth_date
        }
    

    def __str__(self):
        return f"{self.name} {self.surname}"

class WeightMeasure(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    entry_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weight'

    def __str__(self):
        return f'{self.patient.username} - {self.weight} Kg in data {self.entry_date}'

class Food(models.Model):
    name = models.CharField(max_length=256, default='', blank=True, null=True)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00, verbose_name="Quantità (g)")
    calories = models.FloatField(default=0)
    kjoules = models.FloatField(default=0)
    totalfat = models.IntegerField(default=0)
    saturatedfat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    cholestorol = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    sugars = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

    def to_json(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'calories': self.calories,
            'totalfat': self.totalfat,
            'saturatedfat': self.saturatedfat,
            'carbs': self.carbs,
            'cholestorol' : self.cholestorol,       
            'sodium': self.sodium,
            'fiber': self.fiber,
            'sugars': self.sugars,
            'protein': self.protein,

        }

    def __str__(self):
        return f"{self.name}"

class FoodLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.patient.username} - {self.food_consumed.food_name}'

class FoodSubstitute(models.Model):
    food_substitute = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, related_name='food_substitute')
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
    food_to_substitute = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, related_name='food_to_substitute')

    def __str__(self):
        return f'{self.food_substitute} - {self.food_to_substitute} substitute'

    class Meta:
        verbose_name = 'Food Substitute'
        verbose_name_plural = 'Food Substitute'

class Image(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='get_images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.image}'

class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, choices=MEALS, default='colazione')
    foods = models.ManyToManyField(Food)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'foods': self.foods,
            'patient': self.patient,
        }

    def __str__(self):
        return f"{self.patient} - {self.name}"

# Dieta insieme di pasti, ex: colazione, pranzo, cena, merenda
class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    day_of_week = models.CharField(max_length=20, choices=DAY_OF_WEEK, default="Lunedì") 
    meals = models.ManyToManyField(Meal)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'patient': self.patient,
            'day_of_week': self.day_of_week,
            'meals': self.meals
        }

    def __str__(self):
        return f"{self.patient} - {self.day_of_week}"

class PatientProgram(models.Model):

    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)
    dieta = models.ManyToManyField(Diet)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'patient': self.id,
            'is_active': self.id,
            'dieta': self.id,
            'start_date': self.id,
            'end_date': self.id,

        }

    def __str__(self):
        return f"{self.patient}"  
    