from django.contrib import admin
from. models import Patient, Food, Diet, Meal, PatientProgram, FoodSubstitute, Advice, Portion

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['category'] 

class PortionAdmin(admin.ModelAdmin):
    readonly_fields = [
        'total_kcal',
        'total_kj',
        'total_carbohydrates',
        'total_fats',
        'total_proteins',
        'total_water',
        'total_complex_carbohydrates',
        'total_soluble_sugars',
        'total_total_saturated_fats',
        'total_total_monounsaturated_fats',
        'total_total_polyunsaturated_fats',
        'total_cholesterol',
        'total_total_fiber',
        'total_soluble_fiber',
        'total_insoluble_fiber',
        'total_alcohol',
        'total_sodium',
        'total_potassium',
        'total_iron',
        'total_calcium',
        'total_phosphorus',
        'total_magnesium',
        'total_zinc',
        'total_copper',
        'total_selenium',
        'total_thiamine_vitamin_b1',
        'total_riboflavin_vitamin_b2',
        'total_niacin_vitamin_b3',
        'total_vitamin_a_retinol_eq',
        'total_vitamin_c',
        'total_vitamin_e',
        'total_vitamin_b6',
        'total_vitamin_b12',
        'total_manganese',
    ]

class MealAdmin(admin.ModelAdmin):
    readonly_fields = [
        'total_kcal',
        'total_kj',
        'total_carbohydrates',
        'total_fats',
        'total_proteins',
        'total_water',
        'total_complex_carbohydrates',
        'total_soluble_sugars',
        'total_total_saturated_fats',
        'total_total_monounsaturated_fats',
        'total_total_polyunsaturated_fats',
        'total_cholesterol',
        'total_total_fiber',
        'total_soluble_fiber',
        'total_insoluble_fiber',
        'total_alcohol',
        'total_sodium',
        'total_potassium',
        'total_iron',
        'total_calcium',
        'total_phosphorus',
        'total_magnesium',
        'total_zinc',
        'total_copper',
        'total_selenium',
        'total_thiamine_vitamin_b1',
        'total_riboflavin_vitamin_b2',
        'total_niacin_vitamin_b3',
        'total_vitamin_a_retinol_eq',
        'total_vitamin_c',
        'total_vitamin_e',
        'total_vitamin_b6',
        'total_vitamin_b12',
        'total_manganese',
    ]

admin.site.register(Patient)
admin.site.register(Food, FoodAdmin)
admin.site.register(Diet)
admin.site.register(Meal, MealAdmin)
admin.site.register(PatientProgram)
admin.site.register(FoodSubstitute)
admin.site.register(Advice)
admin.site.register(Portion, PortionAdmin)