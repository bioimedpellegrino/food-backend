import pandas as pd
from core.models import Food


def init_data():
    
    df = pd.read_excel("datasource/personal_trainer_scrap.xlsx")
    
    for _, row in df.iterrows():
        
        print(row)

def extract_value_and_unit(text):
    units = ["%", "mg", "µg", "g"]
    strings = ["ND", "Tracce", "", "0"]
    text = str(text)
    if text.strip() in strings:
        return text, ""
    else:
        for unit in units:
            if unit in text:
                value = text.replace(" ", "").replace(unit, "")
                return value, unit
