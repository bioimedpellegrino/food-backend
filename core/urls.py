from django.urls import path
from .views import TestView

urlpatterns = [
    path('api/v1/test/', TestView.as_view(), name='test'),
]