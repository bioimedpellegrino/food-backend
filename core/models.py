from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

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
    weight = models.DecimalField(max_digits=7, decimal_places=4)
    entry_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weight'

    def __str__(self):
        return f'{self.patient.username} - {self.weight} Kg in data {self.entry_date}'

class Food(models.Model):

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
        return f"{self.name - self.category}"


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

    def __str__(self):
        return f"{self.id} - {self.name}"

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

class Portion(models.Model):
    name = models.CharField(max_length=256, default='', blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=7, decimal_places=4, default=0)
    unity = models.CharField(max_length=255, choices=UNITY, default="g", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    @property
    def total_kcal(self):
        return (self.food.kcal / 100) * self.quantity

    @property
    def total_kj(self):
        return (self.food.kj / 100) * self.quantity

    @property
    def total_carbohydrates(self):
        return (self.food.carbohydrates / 100) * self.quantity

    @property
    def total_fats(self):
        return (self.food.fats / 100) * self.quantity

    @property
    def total_proteins(self):
        return (self.food.proteins / 100) * self.quantity

    @property
    def total_water(self):
        return (self.food.water / 100) * self.quantity

    @property
    def total_complex_carbohydrates(self):
        return (self.food.complex_carbohydrates / 100) * self.quantity

    @property
    def total_soluble_sugars(self):
        return (self.food.soluble_sugars / 100) * self.quantity

    @property
    def total_total_saturated_fats(self):
        return (self.food.total_saturated_fats / 100) * self.quantity

    @property
    def total_total_monounsaturated_fats(self):
        return (self.food.total_monounsaturated_fats / 100) * self.quantity

    @property
    def total_total_polyunsaturated_fats(self):
        return (self.food.total_polyunsaturated_fats / 100) * self.quantity

    @property
    def total_cholesterol(self):
        return (self.food.cholesterol / 100) * self.quantity

    @property
    def total_total_fiber(self):
        return (self.food.total_fiber / 100) * self.quantity

    @property
    def total_soluble_fiber(self):
        return (self.food.soluble_fiber / 100) * self.quantity

    @property
    def total_insoluble_fiber(self):
        return (self.food.insoluble_fiber / 100) * self.quantity

    @property
    def total_alcohol(self):
        return (self.food.alcohol / 100) * self.quantity

    @property
    def total_sodium(self):
        return (self.food.sodium / 100) * self.quantity

    @property
    def total_potassium(self):
        return (self.food.potassium / 100) * self.quantity

    @property
    def total_iron(self):
        return (self.food.iron / 100) * self.quantity

    @property
    def total_calcium(self):
        return (self.food.calcium / 100) * self.quantity

    @property
    def total_phosphorus(self):
        return (self.food.phosphorus / 100) * self.quantity

    @property
    def total_magnesium(self):
        return (self.food.magnesium / 100) * self.quantity

    @property
    def total_zinc(self):
        return (self.food.zinc / 100) * self.quantity

    @property
    def total_copper(self):
        return (self.food.copper / 100) * self.quantity

    @property
    def total_selenium(self):
        return (self.food.selenium / 100) * self.quantity

    @property
    def total_thiamine_vitamin_b1(self):
        return (self.food.thiamine_vitamin_b1 / 100) * self.quantity

    @property
    def total_riboflavin_vitamin_b2(self):
        return (self.food.riboflavin_vitamin_b2 / 100) * self.quantity

    @property
    def total_niacin_vitamin_b3(self):
        return (self.food.niacin_vitamin_b3 / 100) * self.quantity

    @property
    def total_vitamin_a_retinol_eq(self):
        return (self.food.vitamin_a_retinol_eq / 100) * self.quantity

    @property
    def total_vitamin_c(self):
        return (self.food.vitamin_c / 100) * self.quantity

    @property
    def total_vitamin_e(self):
        return (self.food.vitamin_e / 100) * self.quantity

    @property
    def total_vitamin_b6(self):
        return (self.food.vitamin_b6 / 100) * self.quantity

    @property
    def total_vitamin_b12(self):
        return (self.food.vitamin_b12 / 100) * self.quantity

    @property
    def total_manganese(self):
        return (self.food.manganese / 100) * self.quantity



class FoodLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.patient.username} - {self.food_consumed.food_name}'

class FoodSubstitute(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    food_to_substitute = models.ForeignKey(Food, default=None,on_delete=models.CASCADE, related_name='food_to_substitute')
    food_substitute = models.ForeignKey(Food, default=None, on_delete=models.CASCADE, related_name='food_substitute')
    substitute_quantity = models.DecimalField(max_digits=7, decimal_places=4, default=100.00)

    def __str__(self):
        return f"\"{self.food_substitute}\" substitution for \"{self.food_to_substitute}\""

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
    portions = models.ManyToManyField(Portion)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'foods': self.foods
        }

    def __str__(self):
        return f"{self.name}"
            
    @property
    def total_kcal(self):
        total_kcal = 0
        for portion in self.portions.all():
            total_kcal += portion.total_kcal
        return total_kcal
        
    @property
    def total_kj(self):
        total_kj = 0
        for portion in self.portions.all():
            total_kj += portion.total_kj
        return total_kj
        
    @property
    def total_carbohydrates(self):
        total_carbohydrates = 0
        for portion in self.portions.all():
            total_carbohydrates += portion.total_carbohydrates
        return total_carbohydrates
        
    @property
    def total_fats(self):
        total_fats = 0
        for portion in self.portions.all():
            total_fats += portion.total_fats
        return total_fats
        
    @property
    def total_proteins(self):
        total_proteins = 0
        for portion in self.portions.all():
            total_proteins += portion.total_proteins
        return total_proteins

    @property
    def total_water(self):
        total_water = 0
        for portion in self.portions.all():
            total_water += portion.total_water
        return total_water
        
    @property
    def total_complex_carbohydrates(self):
        total_complex_carbohydrates = 0
        for portion in self.portions.all():
            total_complex_carbohydrates += portion.total_complex_carbohydrates
        return total_complex_carbohydrates
        
    @property
    def total_soluble_sugars(self):
        total_soluble_sugars = 0
        for portion in self.portions.all():
            total_soluble_sugars += portion.total_soluble_sugars
        return total_soluble_sugars
        
    @property
    def total_total_saturated_fats(self):
        total_total_saturated_fats = 0
        for portion in self.portions.all():
            total_total_saturated_fats += portion.total_total_saturated_fats
        return total_total_saturated_fats
        
    @property
    def total_total_monounsaturated_fats(self):
        total_total_monounsaturated_fats = 0
        for portion in self.portions.all():
            total_total_monounsaturated_fats += portion.total_total_monounsaturated_fats
        return total_total_monounsaturated_fats
        
    @property
    def total_total_polyunsaturated_fats(self):
        total_total_polyunsaturated_fats = 0
        for portion in self.portions.all():
            total_total_polyunsaturated_fats += portion.total_total_polyunsaturated_fats
        return total_total_polyunsaturated_fats
        
    @property
    def total_cholesterol(self):
        total_cholesterol = 0
        for portion in self.portions.all():
            total_cholesterol += portion.total_cholesterol
        return total_cholesterol
        
    @property
    def total_total_fiber(self):
        total_total_fiber = 0
        for portion in self.portions.all():
            total_total_fiber += portion.total_total_fiber
        return total_total_fiber
        
    @property
    def total_soluble_fiber(self):
        total_soluble_fiber = 0
        for portion in self.portions.all():
            total_soluble_fiber += portion.total_soluble_fiber
        return total_soluble_fiber
        
    @property
    def total_insoluble_fiber(self):
        total_insoluble_fiber = 0
        for portion in self.portions.all():
            total_insoluble_fiber += portion.total_insoluble_fiber
        return total_insoluble_fiber
        
    @property
    def total_alcohol(self):
        total_alcohol = 0
        for portion in self.portions.all():
            total_alcohol += portion.total_alcohol
        return total_alcohol
        
    @property
    def total_sodium(self):
        total_sodium = 0
        for portion in self.portions.all():
            total_sodium += portion.total_sodium
        return total_sodium
        
    @property
    def total_potassium(self):
        total_potassium = 0
        for portion in self.portions.all():
            total_potassium += portion.total_potassium
        return total_potassium
        
    @property
    def total_iron(self):
        total_iron = 0
        for portion in self.portions.all():
            total_iron += portion.total_iron
        return total_iron
        
    @property
    def total_calcium(self):
        total_calcium = 0
        for portion in self.portions.all():
            total_calcium += portion.total_calcium
        return total_calcium
        
    @property
    def total_phosphorus(self):
        total_phosphorus = 0
        for portion in self.portions.all():
            total_phosphorus += portion.total_phosphorus
        return total_phosphorus
        
    @property
    def total_magnesium(self):
        total_magnesium = 0
        for portion in self.portions.all():
            total_magnesium += portion.total_magnesium
        return total_magnesium
        
    @property
    def total_zinc(self):
        total_zinc = 0
        for portion in self.portions.all():
            total_zinc += portion.total_zinc
        return total_zinc
        
    @property
    def total_copper(self):
        total_copper = 0
        for portion in self.portions.all():
            total_copper += portion.total_copper
        return total_copper
        
    @property
    def total_selenium(self):
        total_selenium = 0
        for portion in self.portions.all():
            total_selenium += portion.total_selenium
        return total_selenium
        
    @property
    def total_thiamine_vitamin_b1(self):
        total_thiamine_vitamin_b1 = 0
        for portion in self.portions.all():
            total_thiamine_vitamin_b1 += portion.total_thiamine_vitamin_b1
        return total_thiamine_vitamin_b1
        
    @property
    def total_riboflavin_vitamin_b2(self):
        total_riboflavin_vitamin_b2 = 0
        for portion in self.portions.all():
            total_riboflavin_vitamin_b2 += portion.total_riboflavin_vitamin_b2
        return total_riboflavin_vitamin_b2
        
    @property
    def total_niacin_vitamin_b3(self):
        total_niacin_vitamin_b3 = 0
        for portion in self.portions.all():
            total_niacin_vitamin_b3 += portion.total_niacin_vitamin_b3
        return total_niacin_vitamin_b3
        
    @property
    def total_vitamin_a_retinol_eq(self):
        total_vitamin_a_retinol_eq = 0
        for portion in self.portions.all():
            total_vitamin_a_retinol_eq += portion.total_vitamin_a_retinol_eq
        return total_vitamin_a_retinol_eq
        
    @property
    def total_vitamin_c(self):
        total_vitamin_c = 0
        for portion in self.portions.all():
            total_vitamin_c += portion.total_vitamin_c
        return total_vitamin_c
        
    @property
    def total_vitamin_e(self):
        total_vitamin_e = 0
        for portion in self.portions.all():
            total_vitamin_e += portion.total_vitamin_e
        return total_vitamin_e
        
    @property
    def total_vitamin_b6(self):
        total_vitamin_b6 = 0
        for portion in self.portions.all():
            total_vitamin_b6 += portion.total_vitamin_b6
        return total_vitamin_b6
        
    @property
    def total_vitamin_b12(self):
        total_vitamin_b12 = 0
        for portion in self.portions.all():
            total_vitamin_b12 += portion.total_vitamin_b12
        return total_vitamin_b12
        
    @property
    def total_manganese(self):
        total_manganese = 0
        for portion in self.portions.all():
            total_manganese += portion.total_manganese
        return total_manganese
        

 
    
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
    

class Advice(models.Model):
    
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
    
