from django.urls import path
from .views import *

urlpatterns = [
    
    # Patient
    path('patient/info/', PatientView.as_view(), name='patient_info'),
    
    # Food and diet
    path('food/diet/', DailyFoodView.as_view(), name='food_list'),
    path('food/diet/list/', DailyFoodListView.as_view(), name='food_list'),
    path('food/detail/<str:food_id>/', FoodDetailsView.as_view(), name='food_details'),
    path('food/diet/meal_micronutrients/<int:id>/', MealMicronutrientsView.as_view(), name='meal_micro'),
    path('food/get_log_weight_chart/', GetLogWeightData.as_view(), name='get_log_weight_chart'),
    path('food/log_weight/', WeightMeasureView.as_view(), name='log_weight'),
    
    # Advices
    path('advices/', AdvicesListView.as_view(), name='advices_list')
]