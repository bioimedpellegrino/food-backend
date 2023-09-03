from django.urls import path
from .views import *

urlpatterns = [
    path('food/list/', DailyFoodListView.as_view(), name='food_list'),
    path('food/<str:food_id>/', FoodDetailsView.as_view(), name='food_details'),
    path('advices/', AdvicesListView.as_view(), name='advices_list')
]