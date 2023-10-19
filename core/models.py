from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import timedelta

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

MEALS = [("breakfast", "Colazione"),
         ("launch", "Pranzo"),
         ("dinner", "Cena"),
         ("snack_morning", "Spuntino mattina"),
         ("snack_afternoon", "Spuntino pomeriggio"),
         ("before_sleep", "Pre nanna"),
        ]

ADVICE_TYPES = [("Consigli", "Consigli"),
                ("Sostituzioni", "Sostituzioni")]

UNITY = [("g", "g"), ("ml", "ml")]

FOOD_CATEGORIES = [
    ('carni_fresche', 'Carni Fresche'),
    ('verdure_e_ortaggi', 'Verdure e Ortaggi'),
    ('frutta', 'Frutta'),
    ('legumi', 'Legumi'),
    ('cereali_e_derivati', 'Cereali e Derivati'),
    ('carni_trasformate_e_conservate', 'Carni Trasformate e Conservate'),
    ('fast_food_a_base_di_carne', 'Fast-Food a base di carne'),
    ('frattaglie', 'Frattaglie'),
    ('prodotti_della_pesca', 'Prodotti della Pesca'),
    ('latte_e_yogurt', 'Latte e Yogurt'),
    ('formaggi_e_latticini', 'Formaggi e Latticini'),
    ('olii_e_grassi', 'Olii e Grassi'),
    ('uova', 'Uova'),
    ('prodotti_vari', 'Prodotti Vari'),
    ('dolci', 'Dolci'),
    ('bevande_alcooliche', 'Bevande Alcooliche'),
]

class Patient(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256, blank=True, null=True)
    surname = models.CharField(max_length=256, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    phone_prefix = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=4)
    gender = models.CharField(max_length=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date,
            "email": self.email if self.email else "",
            "phone_prefix": self.phone_prefix if self.phone_prefix else "",
            "phone": self.phone if self.phone else "",
            "height": self.height if self.height else 0,
            "weight": self.weight if self.weight else 0,
            "gender": self.gender if self.gender else ""
        }

    class Meta:
        verbose_name  = "Paziente"
        verbose_name_plural = "1. Pazienti"

class WeightMeasure(models.Model):
    
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=4)
    entry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.patient.user.username} - {self.weight} Kg in data {self.entry_date}'
    
    class Meta:
        verbose_name = 'Pesata'
        verbose_name_plural = '10. Pesate'

class Food(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True, help_text="Nome del cibo")
    category = models.CharField(max_length=255, choices=FOOD_CATEGORIES, default='', help_text="Categoria del cibo")
    kcal = models.DecimalField(max_digits=16, decimal_places=4, default=0, help_text="Valore calorico (kcal)")
    kj = models.DecimalField(max_digits=16, decimal_places=4, default=0, help_text="Valore energetico (kJ)")
    carbohydrates = models.DecimalField(max_digits=16, decimal_places=4, default=0, help_text="Carboidrati disponibili (g)")
    fats = models.DecimalField(max_digits=16, decimal_places=4, default=0, help_text="Grassi (g)")
    proteins = models.DecimalField(max_digits=16, decimal_places=4, default=0, help_text="Proteine (g)")
    chemical_composition = models.TextField(help_text="Composizione chimica", blank=True, default='', null=True)
    edible_part = models.CharField(max_length=255, help_text="Parte edibile (%)", default='', blank=True, null=True)
    water = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Contenuto di acqua (g)")
    complex_carbohydrates = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Carboidrati complessi (g)")
    soluble_sugars = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Zuccheri solubili (g)")
    total_saturated_fats = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Saturi totali (g)")
    total_monounsaturated_fats = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Monoinsaturi totali (g)")
    total_polyunsaturated_fats = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Polinsaturi totali (g)")
    cholesterol = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Colesterolo (mg)")
    total_fiber = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Fibra totale (g)")
    soluble_fiber = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Fibra solubile (g)")
    insoluble_fiber = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Fibra insolubile (g)")
    alcohol = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Alcol (g)")
    sodium = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Sodio (mg)")
    potassium = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Potassio (mg)")
    iron = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Ferro (mg)")
    calcium = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Calcio (mg)")
    phosphorus = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Fosforo (mg)")
    magnesium = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Magnesio (mg)")
    zinc = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Zinco (mg)")
    copper = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Rame (mg)")
    selenium = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Selenio (µg)")
    thiamine_vitamin_b1 = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Tiamina (Vit. B1) (mg)")
    riboflavin_vitamin_b2 = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Riboflavina (Vit. B2) (mg)")
    niacin_vitamin_b3 = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Niacina (Vit. B3 o PP) (mg)")
    vitamin_a_retinol_eq = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Vitamina A retinolo eq. (µg)")
    vitamin_c = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Vitamina C (mg)")
    vitamin_e = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Vitamina E (mg)")
    vitamin_b6 = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Vitamina B6 (mg)")
    vitamin_b12 = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Vitamina B12 (mg)")
    manganese = models.DecimalField(max_digits=16, decimal_places=4, blank=True, default=0, null=True, help_text="Manganese (mg)")

    def __str__(self):
        return self.name

    def to_json_small(self):
        
        return {
            'name': self.name,
            'category': self.category,
            'kcal': self.kcal,
            'kj': self.kj,
            'carbohydrates': self.carbohydrates,
            'fats': self.fats,
            'proteins': self.proteins   
        }
        
    def to_json(self):
        
        return {
            'name': self.name,
            'category': self.category,
            'kcal': str(self.kcal),
            'kj': str(self.kj),
            'chemical_composition': self.chemical_composition,
            'edible_part': self.edible_part,
            'water': str(self.water),
            'carbohydrates': str(self.carbohydrates),
            'complex_carbohydrates': str(self.complex_carbohydrates),
            'soluble_sugars': str(self.soluble_sugars),
            'proteins': str(self.proteins),
            'fats': str(self.fats),
            'total_saturated_fats': str(self.total_saturated_fats),
            'total_monounsaturated_fats': str(self.total_monounsaturated_fats),
            'total_polyunsaturated_fats': str(self.total_polyunsaturated_fats),
            'cholesterol': str(self.cholesterol),
            'total_fiber': str(self.total_fiber),
            'soluble_fiber': str(self.soluble_fiber),
            'insoluble_fiber': str(self.insoluble_fiber),
            'alcohol': str(self.alcohol),
            'sodium': str(self.sodium),
            'potassium': str(self.potassium),
            'iron': str(self.iron),
            'calcium': str(self.calcium),
            'phosphorus': str(self.phosphorus),
            'magnesium': str(self.magnesium),
            'zinc': str(self.zinc),
            'copper': str(self.copper),
            'selenium': str(self.selenium),
            'thiamine_vitamin_b1': str(self.thiamine_vitamin_b1),
            'riboflavin_vitamin_b2': str(self.riboflavin_vitamin_b2),
            'niacin_vitamin_b3': str(self.niacin_vitamin_b3),
            'vitamin_a_retinol_eq': str(self.vitamin_a_retinol_eq),
            'vitamin_c': str(self.vitamin_c),
            'vitamin_e': str(self.vitamin_e),
            'vitamin_b6': str(self.vitamin_b6),
            'vitamin_b12': str(self.vitamin_b12),
            'manganese': str(self.manganese),
        }

    @staticmethod
    def get_Food_unity():
    
        return {        
            "kcal": "kcal",
            "kj": "kJ",
            "Carboidrati disponibili": "g",
            "Grassi (Lipidi)": "g",
            "Proteine": "g",
            "Acqua": "g",
            "Carboidrati complessi": "g",
            "Zuccheri solubili": "g",
            "Saturi totali": "g",
            "Monoinsaturi totali": "g",
            "Polinsaturi totali": "g",
            "Colesterolo": "mg",
            "Fibra totale": "g",
            "Fibra solubile": "g",
            "Fibra insolubile": "g",
            "Alcol (g)": "g",
            "Sodio": "mg",
            "Potassio": "mg",
            "Ferro": "mg",
            "Calcio": "mg",
            "Fosforo": "mg",
            "Magnesio": "mg",
            "Zinco": "mg",
            "Rame": "mg",
            "Selenio": "µg",
            "Tiamina (Vit. B1)": "mg",
            "Riboflavina (Vit. B2)": "mg",
            "Niacina (Vit. B3 o PP)": "mg",
            "Vitamina A retinolo eq.": "µg",
            "Vitamina C": "mg",
            "Vitamina E": "mg",
            "Vitamina B6": "mg",
            "Vitamina B12": "mg",
            "Manganese": "mg"
        }
    
    @staticmethod
    def get_food_unity():
    
        return {        
            "kcal": "kcal",
            "kj": "kJ",
            "carbohydrates": "g",
            "fats": "g",
            "proteins": "g",
            "water": "g",
            "complex_carbohydrates": "g",
            "soluble_sugars": "g",
            "total_saturated_fats": "g",
            "total_monounsaturated_fats": "g",
            "total_polyunsaturated_fats": "g",
            "cholesterol": "mg",
            "total_fiber": "g",
            "soluble_fiber": "g",
            "insoluble_fiber": "g",
            "alcohol": "g",
            "sodium": "mg",
            "potassium": "mg",
            "iron": "mg",
            "calcium": "mg",
            "phosphorus": "mg",
            "magnesium": "mg",
            "zinc": "mg",
            "copper": "mg",
            "selenium": "µg",
            "thiamine_vitamin_b1": "mg",
            "riboflavin_vitamin_b2": "mg",
            "niacin_vitamin_b3": "mg",
            "vitamin_a_retinol_eq": "µg",
            "vitamin_c": "mg",
            "vitamin_e": "mg",
            "vitamin_b6": "mg",
            "vitamin_b12": "mg",
            "manganese": "mg"
        }
    
    class Meta:
        verbose_name = "Alimento"
        verbose_name_plural = "3. Alimenti"
        ordering = ('name',)

class Portion(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, default='', blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=7, decimal_places=4, default=0)
    unity = models.CharField(max_length=255, choices=UNITY, default="g", null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{float(round(self.quantity,2))} {self.unity} - {self.name} (KCAL:{self.total_kcal()}, C:{self.total_carbohydrates()}, P:{self.total_proteins()}, G:{self.total_fats()})"
    
    def to_json(self):
        return {
            "name": self.name,
            "food": self.food.id,
            "quantity": float(round(self.quantity, 2)),
            "unity": self.unity,
        }
    
    def to_json_short(self):
        return {
            "id": self.pk,
            "name": self.name,
            "quantity": float(round(self.quantity, 2)),
            "unity": self.unity,
        }
    
    def total_kcal(self):
        return round((self.food.kcal / 100) * self.quantity, 2)

    def total_kj(self):
        return round((self.food.kj / 100) * self.quantity, 2)

    def total_carbohydrates(self):
        return round((self.food.carbohydrates / 100) * self.quantity, 2)

    def total_fats(self):
        return round((self.food.fats / 100) * self.quantity, 2)

    def total_proteins(self):
        return round((self.food.proteins / 100) * self.quantity, 2)

    def total_water(self):
        return round((self.food.water / 100) * self.quantity, 2) if self.food.water else 0

    def total_complex_carbohydrates(self):
        return round((self.food.complex_carbohydrates / 100) * self.quantity, 2) if self.food.complex_carbohydrates else 0

    def total_soluble_sugars(self):
        return round((self.food.soluble_sugars / 100) * self.quantity, 2) if self.food.soluble_sugars else 0

    def total_total_saturated_fats(self):
        return round((self.food.total_saturated_fats / 100) * self.quantity, 2) if self.food.total_saturated_fats else 0

    def total_total_monounsaturated_fats(self):
        return round((self.food.total_monounsaturated_fats / 100) * self.quantity, 2) if self.food.total_monounsaturated_fats else 0

    def total_total_polyunsaturated_fats(self):
        return round((self.food.total_polyunsaturated_fats / 100) * self.quantity, 2) if self.food.total_polyunsaturated_fats else 0

    def total_cholesterol(self):
        return round((self.food.cholesterol / 100) * self.quantity, 2) if self.food.cholesterol else 0

    def total_total_fiber(self):
        return round((self.food.total_fiber / 100) * self.quantity, 2) if self.food.total_fiber else 0

    def total_soluble_fiber(self):
        return round((self.food.soluble_fiber / 100) * self.quantity, 2) if self.food.soluble_fiber else 0

    def total_insoluble_fiber(self):
        return round((self.food.insoluble_fiber / 100) * self.quantity, 2) if self.food.insoluble_fiber else 0

    def total_alcohol(self):
        return round((self.food.alcohol / 100) * self.quantity, 2) if self.food.alcohol else 0

    def total_sodium(self):
        return round((self.food.sodium / 100) * self.quantity, 2) if self.food.sodium else 0

    def total_potassium(self):
        return round((self.food.potassium / 100) * self.quantity, 2) if self.food.potassium else 0

    def total_iron(self):
        return round((self.food.iron / 100) * self.quantity, 2) if self.food.iron else 0

    def total_calcium(self):
        return round((self.food.calcium / 100) * self.quantity, 2) if self.food.calcium else 0

    def total_phosphorus(self):
        return round((self.food.phosphorus / 100) * self.quantity, 2) if self.food.phosphorus else 0

    def total_magnesium(self):
        return round((self.food.magnesium / 100) * self.quantity, 2) if self.food.magnesium else 0

    def total_zinc(self):
        return round((self.food.zinc / 100) * self.quantity, 2) if self.food.zinc else 0

    def total_copper(self):
        return round((self.food.copper / 100) * self.quantity, 2) if self.food.copper else 0

    def total_selenium(self):
        return round((self.food.selenium / 100) * self.quantity, 2) if self.food.selenium else 0

    def total_thiamine_vitamin_b1(self):
        return round((self.food.thiamine_vitamin_b1 / 100) * self.quantity, 2) if self.food.thiamine_vitamin_b1 else 0

    def total_riboflavin_vitamin_b2(self):
        return round((self.food.riboflavin_vitamin_b2 / 100) * self.quantity, 2) if self.food.riboflavin_vitamin_b2 else 0

    def total_niacin_vitamin_b3(self):
        return round((self.food.niacin_vitamin_b3 / 100) * self.quantity, 2) if self.food.niacin_vitamin_b3 else 0

    def total_vitamin_a_retinol_eq(self):
        return round((self.food.vitamin_a_retinol_eq / 100) * self.quantity, 2) if self.food.vitamin_a_retinol_eq else 0

    def total_vitamin_c(self):
        return round((self.food.vitamin_c / 100) * self.quantity, 2) if self.food.vitamin_c else 0

    def total_vitamin_e(self):
        return round((self.food.vitamin_e / 100) * self.quantity, 2) if self.food.vitamin_e else 0

    def total_vitamin_b6(self):
        return round((self.food.vitamin_b6 / 100) * self.quantity, 2) if self.food.vitamin_b6 else 0

    def total_vitamin_b12(self):
        return round((self.food.vitamin_b12 / 100) * self.quantity, 2) if self.food.vitamin_b12 else 0

    def total_manganese(self):
        return round((self.food.manganese / 100) * self.quantity, 2) if self.food.manganese else 0
    
    
    total_kcal.short_description = "Calorie totali (kcal)"
    total_kj.short_description = "Kj Totali (kJ)"
    total_carbohydrates.short_description = "Carboidrati totali (g)"
    total_fats.short_description = "Grassi totali (g)"
    total_proteins.short_description = "Proteine totali (g)"
    total_water.short_description = "Acqua totale (g)"
    total_complex_carbohydrates.short_description = "Carboidrati complessi totali (g)"
    total_soluble_sugars.short_description = "Zuccheri solubili totali (g)"
    total_total_saturated_fats.short_description = "Grassi saturi totali (g)"
    total_total_monounsaturated_fats.short_description = "Grassi monoinsaturi totali (g)"
    total_total_polyunsaturated_fats.short_description = "Grassi polinsaturi totali (g)"
    total_cholesterol.short_description = "Colesterolo totale (mg)"
    total_total_fiber.short_description = "Fibra totale (g)"
    total_soluble_fiber.short_description = "Fibra solubile totale (g)"
    total_insoluble_fiber.short_description = "Fibra insolubile totale (g)"
    total_alcohol.short_description = "Alcol totale (g)"
    total_sodium.short_description = "Sodio totale (mg)"
    total_potassium.short_description = "Potassio totale (mg)"
    total_iron.short_description = "Ferro totale (mg)"
    total_calcium.short_description = "Calcio totale (mg)"
    total_phosphorus.short_description = "Fosforo totale (mg)"
    total_magnesium.short_description = "Magnesio totale (mg)"
    total_zinc.short_description = "Zinco totale (mg)"
    total_copper.short_description = "Rame totale (mg)"
    total_selenium.short_description = "Selenio totale (µg)"
    total_thiamine_vitamin_b1.short_description = "Tiamina (Vit. B1) totale (mg)"
    total_riboflavin_vitamin_b2.short_description = "Riboflavina (Vit. B2) totale (mg)"
    total_niacin_vitamin_b3.short_description = "Niacina (Vit. B3 o PP) totale (mg)"
    total_vitamin_a_retinol_eq.short_description = "Vitamina A retinolo eq. totale (µg)"
    total_vitamin_c.short_description = "Vitamina C totale (mg)"
    total_vitamin_e.short_description = "Vitamina E totale (mg)"
    total_vitamin_b6.short_description = "Vitamina B6 totale (mg)"
    total_vitamin_b12.short_description = "Vitamina B12 totale (mg)"
    total_manganese.short_description = "Manganese totale (mg)"
    
    class Meta:
        verbose_name = "Porzione"
        verbose_name_plural = "4. Porzioni"

class Meal(models.Model):
    
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=256, choices=MEALS, default='colazione')
    name = models.CharField(max_length=256, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    portions = models.ManyToManyField(Portion)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "portions": [portion.to_json() for portion in self.portions.all()]
        }
    
    def to_list_element(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "total_kcal": float(self.total_kcal()),
            "total_carbohydrates": float(self.total_carbohydrates()),
            "total_proteins": float(self.total_proteins()),
            "total_fats": float(self.total_fats()),
            "portions": [portion.to_json_short() for portion in self.portions.all()]
        }
    
    def get_micronutrients(self):
        return {
            "total_water": self.total_water(),
            "total_complex_carbohydrates": self.total_complex_carbohydrates(),
            "total_soluble_sugars": self.total_soluble_sugars(),
            "total_total_saturated_fats": self.total_total_saturated_fats(),
            "total_total_monounsaturated_fats": self.total_total_monounsaturated_fats(),
            "total_total_polyunsaturated_fats": self.total_total_polyunsaturated_fats(),
            "total_cholesterol": self.total_cholesterol(),
            "total_total_fiber": self.total_total_fiber(),
            "total_soluble_fiber": self.total_soluble_fiber(),
            "total_insoluble_fiber": self.total_insoluble_fiber(),
            "total_alcohol": self.total_alcohol(),
            "total_sodium": self.total_sodium(),
            "total_potassium": self.total_potassium(),
            "total_iron": self.total_iron(),
            "total_calcium": self.total_calcium(),
            "total_phosphorus": self.total_phosphorus(),
            "total_magnesium": self.total_magnesium(),
            "total_zinc": self.total_zinc(),
            "total_copper": self.total_copper(),
            "total_selenium": self.total_selenium(),
            "total_thiamine_vitamin_b1": self.total_thiamine_vitamin_b1(),
            "total_riboflavin_vitamin_b2": self.total_riboflavin_vitamin_b2(),
            "total_niacin_vitamin_b3": self.total_niacin_vitamin_b3(),
            "total_vitamin_a_retinol_eq": self.total_vitamin_a_retinol_eq(),
            "total_vitamin_c": self.total_vitamin_c(),
            "total_vitamin_e": self.total_vitamin_e(),
            "total_vitamin_b6": self.total_vitamin_b6(),
            "total_vitamin_b12": self.total_vitamin_b12(),
            "total_manganese": self.total_manganese(),
        }

    def __str__(self):
        return f"{self.name}"
            
    def total_kcal(self):
        total_kcal = 0
        for portion in self.portions.all():
            total_kcal += portion.total_kcal()
        return total_kcal
        
    def total_kj(self):
        total_kj = 0
        for portion in self.portions.all():
            total_kj += portion.total_kj()
        return total_kj
        
    def total_carbohydrates(self):
        total_carbohydrates = 0
        for portion in self.portions.all():
            total_carbohydrates += portion.total_carbohydrates()
        return total_carbohydrates
        
    def total_fats(self):
        total_fats = 0
        for portion in self.portions.all():
            total_fats += portion.total_fats()
        return total_fats
        
    def total_proteins(self):
        total_proteins = 0
        for portion in self.portions.all():
            total_proteins += portion.total_proteins()
        return total_proteins

    def total_water(self):
        total_water = 0
        for portion in self.portions.all():
            total_water += portion.total_water()
        return total_water
        
    def total_complex_carbohydrates(self):
        total_complex_carbohydrates = 0
        for portion in self.portions.all():
            total_complex_carbohydrates += portion.total_complex_carbohydrates()
        return total_complex_carbohydrates
        
    def total_soluble_sugars(self):
        total_soluble_sugars = 0
        for portion in self.portions.all():
            total_soluble_sugars += portion.total_soluble_sugars()
        return total_soluble_sugars
        
    def total_total_saturated_fats(self):
        total_total_saturated_fats = 0
        for portion in self.portions.all():
            total_total_saturated_fats += portion.total_total_saturated_fats()
        return total_total_saturated_fats
        
    def total_total_monounsaturated_fats(self):
        total_total_monounsaturated_fats = 0
        for portion in self.portions.all():
            total_total_monounsaturated_fats += portion.total_total_monounsaturated_fats()
        return total_total_monounsaturated_fats
        
    def total_total_polyunsaturated_fats(self):
        total_total_polyunsaturated_fats = 0
        for portion in self.portions.all():
            total_total_polyunsaturated_fats += portion.total_total_polyunsaturated_fats()
        return total_total_polyunsaturated_fats
        
    def total_cholesterol(self):
        total_cholesterol = 0
        for portion in self.portions.all():
            total_cholesterol += portion.total_cholesterol()
        return total_cholesterol
        
    def total_total_fiber(self):
        total_total_fiber = 0
        for portion in self.portions.all():
            total_total_fiber += portion.total_total_fiber()
        return total_total_fiber
        
    def total_soluble_fiber(self):
        total_soluble_fiber = 0
        for portion in self.portions.all():
            total_soluble_fiber += portion.total_soluble_fiber()
        return total_soluble_fiber
        
    def total_insoluble_fiber(self):
        total_insoluble_fiber = 0
        for portion in self.portions.all():
            total_insoluble_fiber += portion.total_insoluble_fiber()
        return total_insoluble_fiber
        
    def total_alcohol(self):
        total_alcohol = 0
        for portion in self.portions.all():
            total_alcohol += portion.total_alcohol()
        return total_alcohol
        
    def total_sodium(self):
        total_sodium = 0
        for portion in self.portions.all():
            total_sodium += portion.total_sodium()
        return total_sodium
        
    def total_potassium(self):
        total_potassium = 0
        for portion in self.portions.all():
            total_potassium += portion.total_potassium()
        return total_potassium
        
    def total_iron(self):
        total_iron = 0
        for portion in self.portions.all():
            total_iron += portion.total_iron()
        return total_iron
        
    def total_calcium(self):
        total_calcium = 0
        for portion in self.portions.all():
            total_calcium += portion.total_calcium()
        return total_calcium
        
    def total_phosphorus(self):
        total_phosphorus = 0
        for portion in self.portions.all():
            total_phosphorus += portion.total_phosphorus()
        return total_phosphorus
        
    def total_magnesium(self):
        total_magnesium = 0
        for portion in self.portions.all():
            total_magnesium += portion.total_magnesium()
        return total_magnesium
        
    def total_zinc(self):
        total_zinc = 0
        for portion in self.portions.all():
            total_zinc += portion.total_zinc()
        return total_zinc
        
    def total_copper(self):
        total_copper = 0
        for portion in self.portions.all():
            total_copper += portion.total_copper()
        return total_copper
        
    def total_selenium(self):
        total_selenium = 0
        for portion in self.portions.all():
            total_selenium += portion.total_selenium()
        return total_selenium
        
    def total_thiamine_vitamin_b1(self):
        total_thiamine_vitamin_b1 = 0
        for portion in self.portions.all():
            total_thiamine_vitamin_b1 += portion.total_thiamine_vitamin_b1()
        return total_thiamine_vitamin_b1
        
    def total_riboflavin_vitamin_b2(self):
        total_riboflavin_vitamin_b2 = 0
        for portion in self.portions.all():
            total_riboflavin_vitamin_b2 += portion.total_riboflavin_vitamin_b2()
        return total_riboflavin_vitamin_b2
        
    def total_niacin_vitamin_b3(self):
        total_niacin_vitamin_b3 = 0
        for portion in self.portions.all():
            total_niacin_vitamin_b3 += portion.total_niacin_vitamin_b3()
        return total_niacin_vitamin_b3
        
    def total_vitamin_a_retinol_eq(self):
        total_vitamin_a_retinol_eq = 0
        for portion in self.portions.all():
            total_vitamin_a_retinol_eq += portion.total_vitamin_a_retinol_eq()
        return total_vitamin_a_retinol_eq
        
    def total_vitamin_c(self):
        total_vitamin_c = 0
        for portion in self.portions.all():
            total_vitamin_c += portion.total_vitamin_c()
        return total_vitamin_c
        
    def total_vitamin_e(self):
        total_vitamin_e = 0
        for portion in self.portions.all():
            total_vitamin_e += portion.total_vitamin_e()
        return total_vitamin_e
        
    def total_vitamin_b6(self):
        total_vitamin_b6 = 0
        for portion in self.portions.all():
            total_vitamin_b6 += portion.total_vitamin_b6()
        return total_vitamin_b6
        
    def total_vitamin_b12(self):
        total_vitamin_b12 = 0
        for portion in self.portions.all():
            total_vitamin_b12 += portion.total_vitamin_b12()
        return total_vitamin_b12
        
    def total_manganese(self):
        total_manganese = 0
        for portion in self.portions.all():
            total_manganese += portion.total_manganese()
        return total_manganese
    
    total_kcal.short_description = "Calorie totali (kcal)"
    total_kj.short_description = "Kj Totali (kJ)"
    total_carbohydrates.short_description = "Carboidrati totali (g)"
    total_fats.short_description = "Grassi totali (g)"
    total_proteins.short_description = "Proteine totali (g)"
    total_water.short_description = "Acqua totale (g)"
    total_complex_carbohydrates.short_description = "Carboidrati complessi totali (g)"
    total_soluble_sugars.short_description = "Zuccheri solubili totali (g)"
    total_total_saturated_fats.short_description = "Grassi saturi totali (g)"
    total_total_monounsaturated_fats.short_description = "Grassi monoinsaturi totali (g)"
    total_total_polyunsaturated_fats.short_description = "Grassi polinsaturi totali (g)"
    total_cholesterol.short_description = "Colesterolo totale (mg)"
    total_total_fiber.short_description = "Fibra totale (g)"
    total_soluble_fiber.short_description = "Fibra solubile totale (g)"
    total_insoluble_fiber.short_description = "Fibra insolubile totale (g)"
    total_alcohol.short_description = "Alcol totale (g)"
    total_sodium.short_description = "Sodio totale (mg)"
    total_potassium.short_description = "Potassio totale (mg)"
    total_iron.short_description = "Ferro totale (mg)"
    total_calcium.short_description = "Calcio totale (mg)"
    total_phosphorus.short_description = "Fosforo totale (mg)"
    total_magnesium.short_description = "Magnesio totale (mg)"
    total_zinc.short_description = "Zinco totale (mg)"
    total_copper.short_description = "Rame totale (mg)"
    total_selenium.short_description = "Selenio totale (µg)"
    total_thiamine_vitamin_b1.short_description = "Tiamina (Vit. B1) totale (mg)"
    total_riboflavin_vitamin_b2.short_description = "Riboflavina (Vit. B2) totale (mg)"
    total_niacin_vitamin_b3.short_description = "Niacina (Vit. B3 o PP) totale (mg)"
    total_vitamin_a_retinol_eq.short_description = "Vitamina A retinolo eq. totale (µg)"
    total_vitamin_c.short_description = "Vitamina C totale (mg)"
    total_vitamin_e.short_description = "Vitamina E totale (mg)"
    total_vitamin_b6.short_description = "Vitamina B6 totale (mg)"
    total_vitamin_b12.short_description = "Vitamina B12 totale (mg)"
    total_manganese.short_description = "Manganese totale (mg)"

    class Meta:
        verbose_name = "Pasto"
        verbose_name_plural = "5. Pasti"
        
class DailyDiet(models.Model):
    # Dieta insieme di pasti, ex: colazione, pranzo, cena, merenda
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    meals = models.ManyToManyField(Meal)
    note = models.TextField(blank=True, null=True, default='')
    # Not so elegant but efficient 
    monday = models.BooleanField(default=False, verbose_name="Lunedì")
    tuesday = models.BooleanField(default=False, verbose_name="Martedì")
    wednesday = models.BooleanField(default=False, verbose_name="Mercoledì")
    thursday = models.BooleanField(default=False, verbose_name="Giovedì")
    friday = models.BooleanField(default=False, verbose_name="Venerdì")
    saturday = models.BooleanField(default=False, verbose_name="Sabato")
    sunday = models.BooleanField(default=False, verbose_name="Domenica")

    def __str__(self):
        return f"{self.name}"
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "note": self.note,
            "monday": self.monday,
            "tuesday": self.tuesday,
            "wednesday": self.wednesday,
            "thursday": self.thursday,
            "friday": self.friday,
            "saturday": self.saturday,
            "sunday": self.sunday,
            "meals": [meal.to_json for meal in self.meals.all()]
        }
    
    def clone(self):
        meals = self.meals.all()
        self.id = None
        self.save()

        for item in meals:
            self.meals.add(item)

        self.save()
    
    def total_kcal(self):
        total_kcal = 0
        for meal in self.meals.all():
            total_kcal += meal.total_kcal()
        return total_kcal
        
    def total_kj(self):
        total_kj = 0
        for meal in self.meals.all():
            total_kj += meal.total_kj()
        return total_kj
        
    def total_carbohydrates(self):
        total_carbohydrates = 0
        for meal in self.meals.all():
            total_carbohydrates += meal.total_carbohydrates()
        return total_carbohydrates
        
    def total_fats(self):
        total_fats = 0
        for meal in self.meals.all():
            total_fats += meal.total_fats()
        return total_fats
        
    def total_proteins(self):
        total_proteins = 0
        for meal in self.meals.all():
            total_proteins += meal.total_proteins()
        return total_proteins

    def total_water(self):
        total_water = 0
        for meal in self.meals.all():
            total_water += meal.total_water()
        return total_water
        
    def total_complex_carbohydrates(self):
        total_complex_carbohydrates = 0
        for meal in self.meals.all():
            total_complex_carbohydrates += meal.total_complex_carbohydrates()
        return total_complex_carbohydrates
        
    def total_soluble_sugars(self):
        total_soluble_sugars = 0
        for meal in self.meals.all():
            total_soluble_sugars += meal.total_soluble_sugars()
        return total_soluble_sugars
        
    def total_total_saturated_fats(self):
        total_total_saturated_fats = 0
        for meal in self.meals.all():
            total_total_saturated_fats += meal.total_total_saturated_fats()
        return total_total_saturated_fats
        
    def total_total_monounsaturated_fats(self):
        total_total_monounsaturated_fats = 0
        for meal in self.meals.all():
            total_total_monounsaturated_fats += meal.total_total_monounsaturated_fats()
        return total_total_monounsaturated_fats
        
    def total_total_polyunsaturated_fats(self):
        total_total_polyunsaturated_fats = 0
        for meal in self.meals.all():
            total_total_polyunsaturated_fats += meal.total_total_polyunsaturated_fats()
        return total_total_polyunsaturated_fats
        
    def total_cholesterol(self):
        total_cholesterol = 0
        for meal in self.meals.all():
            total_cholesterol += meal.total_cholesterol()
        return total_cholesterol
        
    def total_total_fiber(self):
        total_total_fiber = 0
        for meal in self.meals.all():
            total_total_fiber += meal.total_total_fiber()
        return total_total_fiber
        
    def total_soluble_fiber(self):
        total_soluble_fiber = 0
        for meal in self.meals.all():
            total_soluble_fiber += meal.total_soluble_fiber()
        return total_soluble_fiber
        
    def total_insoluble_fiber(self):
        total_insoluble_fiber = 0
        for meal in self.meals.all():
            total_insoluble_fiber += meal.total_insoluble_fiber()
        return total_insoluble_fiber
        
    def total_alcohol(self):
        total_alcohol = 0
        for meal in self.meals.all():
            total_alcohol += meal.total_alcohol()
        return total_alcohol
        
    def total_sodium(self):
        total_sodium = 0
        for meal in self.meals.all():
            total_sodium += meal.total_sodium()
        return total_sodium
        
    def total_potassium(self):
        total_potassium = 0
        for meal in self.meals.all():
            total_potassium += meal.total_potassium()
        return total_potassium
        
    def total_iron(self):
        total_iron = 0
        for meal in self.meals.all():
            total_iron += meal.total_iron()
        return total_iron
        
    def total_calcium(self):
        total_calcium = 0
        for meal in self.meals.all():
            total_calcium += meal.total_calcium()
        return total_calcium
        
    def total_phosphorus(self):
        total_phosphorus = 0
        for meal in self.meals.all():
            total_phosphorus += meal.total_phosphorus()
        return total_phosphorus
        
    def total_magnesium(self):
        total_magnesium = 0
        for meal in self.meals.all():
            total_magnesium += meal.total_magnesium()
        return total_magnesium
        
    def total_zinc(self):
        total_zinc = 0
        for meal in self.meals.all():
            total_zinc += meal.total_zinc()
        return total_zinc
        
    def total_copper(self):
        total_copper = 0
        for meal in self.meals.all():
            total_copper += meal.total_copper()
        return total_copper
        
    def total_selenium(self):
        total_selenium = 0
        for meal in self.meals.all():
            total_selenium += meal.total_selenium()
        return total_selenium
        
    def total_thiamine_vitamin_b1(self):
        total_thiamine_vitamin_b1 = 0
        for meal in self.meals.all():
            total_thiamine_vitamin_b1 += meal.total_thiamine_vitamin_b1()
        return total_thiamine_vitamin_b1
        
    def total_riboflavin_vitamin_b2(self):
        total_riboflavin_vitamin_b2 = 0
        for meal in self.meals.all():
            total_riboflavin_vitamin_b2 += meal.total_riboflavin_vitamin_b2()
        return total_riboflavin_vitamin_b2
        
    def total_niacin_vitamin_b3(self):
        total_niacin_vitamin_b3 = 0
        for meal in self.meals.all():
            total_niacin_vitamin_b3 += meal.total_niacin_vitamin_b3()
        return total_niacin_vitamin_b3
        
    def total_vitamin_a_retinol_eq(self):
        total_vitamin_a_retinol_eq = 0
        for meal in self.meals.all():
            total_vitamin_a_retinol_eq += meal.total_vitamin_a_retinol_eq()
        return total_vitamin_a_retinol_eq
        
    def total_vitamin_c(self):
        total_vitamin_c = 0
        for meal in self.meals.all():
            total_vitamin_c += meal.total_vitamin_c()
        return total_vitamin_c
        
    def total_vitamin_e(self):
        total_vitamin_e = 0
        for meal in self.meals.all():
            total_vitamin_e += meal.total_vitamin_e()
        return total_vitamin_e
        
    def total_vitamin_b6(self):
        total_vitamin_b6 = 0
        for meal in self.meals.all():
            total_vitamin_b6 += meal.total_vitamin_b6()
        return total_vitamin_b6
        
    def total_vitamin_b12(self):
        total_vitamin_b12 = 0
        for meal in self.meals.all():
            total_vitamin_b12 += meal.total_vitamin_b12()
        return total_vitamin_b12
        
    def total_manganese(self):
        total_manganese = 0
        for meal in self.meals.all():
            total_manganese += meal.total_manganese()
        return total_manganese
    
    total_kcal.short_description = "Calorie totali (kcal)"
    total_kj.short_description = "Kj Totali (kJ)"
    total_carbohydrates.short_description = "Carboidrati totali (g)"
    total_fats.short_description = "Grassi totali (g)"
    total_proteins.short_description = "Proteine totali (g)"
    total_water.short_description = "Acqua totale (g)"
    total_complex_carbohydrates.short_description = "Carboidrati complessi totali (g)"
    total_soluble_sugars.short_description = "Zuccheri solubili totali (g)"
    total_total_saturated_fats.short_description = "Grassi saturi totali (g)"
    total_total_monounsaturated_fats.short_description = "Grassi monoinsaturi totali (g)"
    total_total_polyunsaturated_fats.short_description = "Grassi polinsaturi totali (g)"
    total_cholesterol.short_description = "Colesterolo totale (mg)"
    total_total_fiber.short_description = "Fibra totale (g)"
    total_soluble_fiber.short_description = "Fibra solubile totale (g)"
    total_insoluble_fiber.short_description = "Fibra insolubile totale (g)"
    total_alcohol.short_description = "Alcol totale (g)"
    total_sodium.short_description = "Sodio totale (mg)"
    total_potassium.short_description = "Potassio totale (mg)"
    total_iron.short_description = "Ferro totale (mg)"
    total_calcium.short_description = "Calcio totale (mg)"
    total_phosphorus.short_description = "Fosforo totale (mg)"
    total_magnesium.short_description = "Magnesio totale (mg)"
    total_zinc.short_description = "Zinco totale (mg)"
    total_copper.short_description = "Rame totale (mg)"
    total_selenium.short_description = "Selenio totale (µg)"
    total_thiamine_vitamin_b1.short_description = "Tiamina (Vit. B1) totale (mg)"
    total_riboflavin_vitamin_b2.short_description = "Riboflavina (Vit. B2) totale (mg)"
    total_niacin_vitamin_b3.short_description = "Niacina (Vit. B3 o PP) totale (mg)"
    total_vitamin_a_retinol_eq.short_description = "Vitamina A retinolo eq. totale (µg)"
    total_vitamin_c.short_description = "Vitamina C totale (mg)"
    total_vitamin_e.short_description = "Vitamina E totale (mg)"
    total_vitamin_b6.short_description = "Vitamina B6 totale (mg)"
    total_vitamin_b12.short_description = "Vitamina B12 totale (mg)"
    total_manganese.short_description = "Manganese totale (mg)"

    class Meta:
        verbose_name = "Dieta giornaliera"
        verbose_name_plural = "6. Diete giornaliere"

class PatientProgram(models.Model):

    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)
    daily_meals = models.ManyToManyField(DailyDiet)
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
    
    def get_date_meals(self, diet_date):
        meals = self.daily_meals.all()
        daily_diet = meals.filter(**{diet_date.strftime("%A").lower(): True}).first()
        if daily_diet:
            return [meal.to_list_element() for meal in daily_diet.meals.all()]
        else:
            return []
        
    def get_ordered_meals(self, start_date, end_date):
        
        ordered_meals = {}
        delta = end_date - start_date
        meals = self.daily_meals.all()
        for i in range(delta.days + 1):
            current_date = start_date + timedelta(days=i)
            daily_diet = meals.filter(**{current_date.strftime("%A").lower(): True}).first()

            if daily_diet:
                # If a daily diet is found, add it to the ordered meals dictionary
                ordered_meals[current_date.strftime("%Y/%m/%d")] = [meal.to_list_element() for meal in daily_diet.meals.all()]
            else:
                # If no daily diet is found, add an empty list to indicate no meals for the day
                ordered_meals[current_date] = []

        return ordered_meals
    
    def monday(self):
        monday_diet = self.daily_meals.filter(monday=True).first()        
        return monday_diet.name
    
    def tuesday(self):
        tuesday_diet = self.daily_meals.filter(tuesday=True).first()
        return tuesday_diet.name

    def wednesday(self):
        wednesday_diet = self.daily_meals.filter(wednesday=True).first()
        return wednesday_diet.name

    def thursday(self):
        thursday_diet = self.daily_meals.filter(thursday=True).first()
        return thursday_diet.name

    def friday(self):
        friday_diet = self.daily_meals.filter(friday=True).first()
        return friday_diet.name

    def saturday(self):
        saturday_diet = self.daily_meals.filter(saturday=True).first()
        return saturday_diet.name

    def sunday(self):
        sunday_diet = self.daily_meals.filter(sunday=True).first()
        return sunday_diet.name
    
    
    monday.short_description = "Dieta del Lunedì"
    tuesday.short_description = "Dieta del Martedì"
    wednesday.short_description = "Dieta del Mercoledì"
    thursday.short_description = "Dieta del Giovedì"
    friday.short_description = "Dieta del Venerdì"
    saturday.short_description = "Dieta del Sabato"
    sunday.short_description = "Dieta della Domenica"

    class Meta:
        verbose_name = "Programma"
        verbose_name_plural = "7. Programmi"
    

class FoodLog(models.Model):
    
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient.username} - {self.food_consumed.food_name}'
    
    class Meta:
        verbose_name = 'Log pasto'
        verbose_name_plural = '8. Log pasti'

class FoodSubstitute(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    food_to_substitute = models.ForeignKey(Food, default=None,on_delete=models.CASCADE, related_name='food_to_substitute')
    food_substitute = models.ForeignKey(Food, default=None, on_delete=models.CASCADE, related_name='food_substitute')
    substitute_quantity = models.DecimalField(max_digits=7, decimal_places=4, default=100.00)

    def __str__(self):
        return f"\"{self.food_substitute}\" substitution for \"{self.food_to_substitute}\""

    class Meta:
        verbose_name = 'Sostituzione'
        verbose_name_plural = '9. Sostituzione pasto'

class Advice(models.Model):
    
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='advice/')
    type =  models.CharField(max_length=256, choices=ADVICE_TYPES, default='advice')
    is_active = models.BooleanField(default=True)
    expire_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "image": self.image.url,
            "type": self.type,
            "time": f"{self.created.strftime('%Y/%m/%d')}"
        }
    
    class Meta:
        verbose_name = 'Consiglio'
        verbose_name_plural = 'Consigli / Articoli per APP'
    
