from django.urls import path
from .views import *

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('food/list', FoodListView.as_view(), name='food_list'),
    path('food/<str:food_id>', FoodDetailsView.as_view(), name='food_details'),
]