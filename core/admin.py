from django.contrib import admin
from. models import Patient, Food, DailyDiet, Meal, PatientProgram, FoodSubstitute, Advice, Portion, WeightMeasure

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['category'] 

class PortionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['food']
    list_display = ['name', 'total_kcal', 'total_carbohydrates', 'total_fats', 'total_proteins']
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
    search_fields = ['name']
    autocomplete_fields = ['portions']
    list_display = ['name', 'total_kcal', 'total_carbohydrates', 'total_fats', 'total_proteins']
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

class DailyMealAdmin(admin.ModelAdmin):
    search_fields = ['id','name']
    list_filter = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    autocomplete_fields = ['meals']
    list_display = ['id','name', 'total_kcal', 'total_carbohydrates', 'total_fats', 'total_proteins']
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
    
    def clone_selected(self, request, queryset):
        for obj in queryset:
            obj.clone()
        self.message_user(request, "Gli elementi selezionati sono stati clonati con successo.")
    clone_selected.short_description = "Clona gli elementi selezionati"
    
    actions = [clone_selected]

class PatientProgramAdmin(admin.ModelAdmin):
    list_filter = ['patient', 'is_active']
    autocomplete_fields = ['daily_meals']
    readonly_fields = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]
    list_display = ['patient', 'start_date', 'end_date']

class WeightMeasureAdmin(admin.ModelAdmin):
    list_filter = ['patient']
    list_display = ['patient', 'weight', 'entry_date']

admin.site.register(Patient)
admin.site.register(Food, FoodAdmin)
admin.site.register(DailyDiet, DailyMealAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(PatientProgram, PatientProgramAdmin)
admin.site.register(FoodSubstitute)
admin.site.register(Advice)
admin.site.register(Portion, PortionAdmin)
admin.site.register(WeightMeasure, WeightMeasureAdmin)