import pandas as pd
import datetime
from tqdm import tqdm
from core.models import Food, Portion, Patient
from django.contrib.auth.models import User

CATEGORIES = {
   "Carni Fresche":"carni_fresche",
   "Verdure e Ortaggi":"verdure_e_ortaggi",
   "Frutta":"frutta",
   "Legumi":"legumi",
   "Cereali e Derivati":"cereali_e_derivati",
   "Carni Trasformate e Conservate":"carni_trasformate_e_conservate",
   "Fast-Food a base di carne":"fast_food_a_base_di_carne",
   "Frattaglie":"frattaglie",
   "Prodotti della pesca":"prodotti_della_pesca",
   "Latte e Yogurt":"latte_e_yogurt",
   "Formaggi e latticini":"formaggi_e_latticini",
   "Olii e Grassi":"olii_e_grassi",
   "Uova":"uova",
   "Prodotti Vari":"prodotti_vari",
   "Dolci":"dolci",
   "Bevande Alcooliche":"bevande_alcooliche"
}

def init_foods():
    
    df = pd.read_excel("datasource/personal_trainer_scrap.xlsx")
    
    food_unity = Food.get_Food_unity()
    
    for _, row in tqdm(df.iterrows()):
        food, cre = Food.objects.get_or_create(name=row['name'])
        food.name = row['name']
        food.category = CATEGORIES[row['category']]
        food.chemical_composition = row['Composizione chimica']
        food.edible_part = row['Parte edibile']
        food.kcal = float(row["kcal"].strip().replace("kcal", "").replace(",", "."))
        food.kj = float(row["kj"].strip().replace("kj", "").replace(",", "."))
        food.carbohydrates = extract_value_and_unit(row["Carboidrati disponibili"])
        food.fats = extract_value_and_unit(row["Grassi (Lipidi)"])
        food.proteins = extract_value_and_unit(row["Proteine"])
        food.water = extract_value_and_unit(row["Acqua"])
        food.complex_carbohydrates = extract_value_and_unit(row["Carboidrati complessi"])
        food.soluble_sugars = extract_value_and_unit(row["Zuccheri solubili"])
        food.total_saturated_fats = extract_value_and_unit(row["Saturi totali"])
        food.total_monounsaturated_fats = extract_value_and_unit(row["Monoinsaturi totali"])
        food.total_polyunsaturated_fats = extract_value_and_unit(row["Polinsaturi totali"])
        food.cholesterol = extract_value_and_unit(row["Colesterolo"])
        food.total_fiber = extract_value_and_unit(row["Fibra totale"])
        food.soluble_fiber = extract_value_and_unit(row["Fibra solubile"])
        food.insoluble_fiber = extract_value_and_unit(row["Fibra insolubile"])
        food.alcohol = extract_value_and_unit(row["Alcol (g)"])
        food.sodium = extract_value_and_unit(row["Sodio"])
        food.potassium = extract_value_and_unit(row["Potassio"])
        food.iron = extract_value_and_unit(row["Ferro"])
        food.calcium = extract_value_and_unit(row["Calcio"])
        food.phosphorus = extract_value_and_unit(row["Fosforo"])
        food.magnesium = extract_value_and_unit(row["Magnesio"])
        food.zinc = extract_value_and_unit(row["Zinco"])
        food.copper = extract_value_and_unit(row["Rame"])
        food.selenium = extract_value_and_unit(row["Selenio"])
        food.thiamine_vitamin_b1 = extract_value_and_unit(row["Tiamina (Vit. B1)"])
        food.riboflavin_vitamin_b2 = extract_value_and_unit(row["Riboflavina (Vit. B2)"])
        food.niacin_vitamin_b3 = extract_value_and_unit(row["Niacina (Vit. B3 o PP)"])
        food.vitamin_a_retinol_eq = extract_value_and_unit(row["Vitamina A retinolo eq."])
        food.vitamin_c = extract_value_and_unit(row["Vitamina C"])
        food.vitamin_e = extract_value_and_unit(row["Vitamina E"])
        food.vitamin_b6 = extract_value_and_unit(row["Vitamina B6"])
        food.vitamin_b12 = extract_value_and_unit(row["Vitamina B12"])
        food.manganese = extract_value_and_unit(row["Manganese"])
        food.save()
        

def init_portions():
    
    foods = Food.objects.all()
    
    for food in tqdm(foods):
        for quantity in range(10, 260, 10):
            name = food.name
            p = Portion()
            p.name = name
            p.quantity = quantity
            p.unity = "g"
            p.food = food
            p.save()

def init_patient():
    
    patient = Patient()
    patient.name = "Alessandro"
    patient.surname = "Pellegrino"
    patient.birth_date = datetime.datetime(1994, 2, 1).date()
    patient.user = User.objects.get(pk=1)
    patient.save()
    
def init_data():
    init_foods()
    init_patient()
    init_portions()

def extract_value_and_unit(text):
    units = ["%", "mg", "µg", "g"]
    strings = ["ND", "", "0"]
    text = str(text).strip()
    if text == 'Tracce' or text == 'tr':
        return 0.001
    elif text in strings:
        return 0
    else:
        for unit in units:
            if unit in text:
                value = text.replace(" ", "").replace(unit, "").replace(",", ".")
                return float(value)
