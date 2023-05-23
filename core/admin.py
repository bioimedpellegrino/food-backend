from django.contrib import admin
from. models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(Food)
admin.site.register(FoodSubstitute)
admin.site.register(Diet)
admin.site.register(Meal)
admin.site.register(PatientProgram)