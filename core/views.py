from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .models import Patient, Food, DailyDiet, Meal, PatientProgram, FoodSubstitute, Advice
from .forms import *
import numpy as np
import traceback
from django.core.files.base import ContentFile
import base64
from .utils import *
import json
import datetime

class DailyFoodListView(APIView):
    
    #dalla request prendo il patient (request.user)
    def get(self, request, *args, **kwargs):
                
        try:
            patient = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            return JsonResponse({"error": "Paziente non trovato"}, status=status.HTTP_404_NOT_FOUND)
        
        days_to_fetch = 10
        
        start_date = datetime.datetime.now().date()
        end_date = start_date + datetime.timedelta(days=days_to_fetch)
        patient_program = PatientProgram.objects.filter(Q(start_date__lte=start_date) & Q(end_date__gte=start_date), patient=patient, is_active=True).first()
        
        results = patient_program.get_ordered_meals(start_date, end_date)
        
        return JsonResponse(results, safe=False)

class FoodDetailsView(APIView):

    def get(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        food_id = kwargs['food_id']
        if food_id:
            try:
                food = Food.objects.get(id=food_id)
                food_data = model_to_dict(food)
                substitutes = FoodSubstitute.objects.filter(food=food_id)
                food_data['substitutes'] = [model_to_dict(substitute) for substitute in substitutes]
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=404) #Cibo non trovato
        else:
            foods = Food.objects.all()
            foods_list = [model_to_dict(food) for food in foods]
            return JsonResponse(foods_list, safe=False)
        
        return render(request, 'food.html', {
            'food': food,
            'images': food.get_images.all(),
        })
    

class AdvicesListView(APIView):
    
    def get(self, request, *args, **kwargs):
        
        today = datetime.datetime.now().date()
        advices = Advice.objects.filter(is_active=True, expire_date__gte=today)
        results = [advice.to_json() for advice in advices]
        return JsonResponse(results, status=200, safe=False)
        
