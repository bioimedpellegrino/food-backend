from django.contrib import admin
from. models import *

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Patient)
<<<<<<< HEAD
admin.site.register(Food)
admin.site.register(FoodSubstitute)
=======
admin.site.register(Food, FoodAdmin)
>>>>>>> f17dc3bd1bf8dbf991c489083cc08fe531ddd6ab
admin.site.register(Diet)
admin.site.register(Meal)
admin.site.register(PatientProgram)
admin.site.register(FoodSubstitute)

