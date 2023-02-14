import pandas as pd
from core.models import Food

df = pd.read_csv('datasource/import_data.csv', sep=',', header=0)

for food in df.iterrows():
    try:
        food_name = food[1][0]
        food_calories = float(food[1][1].replace(',', '.'))
        food_kjoules = float(food[1][2].replace(',', '.'))
        print(food_calories)
        f = Food(name=food_name, calories=int(food_calories))
        print('Adding food: ' + str(food))
        f.save()
    except Exception as e:
        print(e)

