from .models import *

def get_substitute(food):
    output = {}
    try:
        food_item = Food.objects.get(name=food.name)
        print(food)
        print('---food_item', food_item)
        substitute_item = FoodSubstitute.objects.get(food_to_substitute=food)
        output['substitute'] = substitute_item.food_substitute.name
        output['quantity'] = substitute_item.substitute_quantity

    except FoodSubstitute.DoesNotExist:
        # Se FoodSubstitute non viene trovato, restituisci un valore di default
        output['substitute'] = 'Nessun sostituto disponibile'
        output['quantity'] = 'N/A'

    except Exception as e:
        print(e)
        output = {}

    return output

    

    

