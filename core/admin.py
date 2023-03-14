from django.contrib import admin
from. models import *

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Patient)
admin.site.register(Food, FoodAdmin)
admin.site.register(Diet)
admin.site.register(Meal)
admin.site.register(PatientProgram)
admin.site.register(FoodSubstitute)

