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
from .models import Patient, Food, Diet, Meal, PatientProgram, FoodSubstitute, Advice
from .forms import *
import numpy as np
import traceback
from django.core.files.base import ContentFile
import base64
from .utils import *
import json
import datetime

# from tensorflow.keras.models import model_from_json


class ImageUploadView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data()
            print(request.data['b64Data'][:100])
            imgstr = request.data['b64Data']#.split(';base64,') 
            ext = 'png'

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext) 
            # i = Image()
            # i.image=data
            # i.save()

            model_path = 'model.json'
            # loaded_model = model_from_json(model_path)
            # loaded_model.load_weights()
            # #modify the placeholders with the real solutions
            # i.response = my_response['response']
            # i.soulutions = "placeholder_solutions",  #placeholder
            # i.percentage = int(my_response['accuracy'])
            # if request.user.is_authenticated:
            #     i.user = request.user
            # i.save()

            # print(float(i.percentage), i.response)
            # if float(i.percentage) < 85 and i.response == 'positive':
            #     my_response['response'] = 'negative'
            
            # results = {
            #     "response" : my_response['response'],
            #     "solutions" : "placeholder_solutions",  #placeholder
            #     "percentage" : my_response['accuracy']
            # }
            # print(results)
            # return Response(results, status=200)
        except:
            traceback.print_exc()
            results = {
                "response" : 'error',
                "solutions" : "placeholder_solutions",  #placeholder
                "percentage" :  'error',
                'result': traceback.format_exc()
            }
            return Response(results)

class TestView(APIView):
    
    def get(self, request, *args, **kwargs):
        print(request.user, request.data)
        return Response({'test'}, status=200)

class DailyFoodListView(APIView):
    
    #dalla request prendo il patient (request.user)
    def get(self, request, *args, **kwargs):
                
        print(User.objects.all())   
        request_patient = self.request.query_params.get('patient')
        request_day = self.request.query_params.get('day')
        print('---request_day', request_day)
        user = User.objects.get(username=request_patient)
        patient = Patient.objects.get(user=User.objects.get(username=user.username))

        print('---request_day', request_day)

        # Faccio la query sul giorno e prendo i pasti con rispettivi cibi per quel giorno
        diet = Diet.objects.get(patient=patient, day_of_week=request_day)
        

        diet_response = {
            'dieta_giornaliera': str(patient) + ' - ' + str(request_day),
            'meals': [
            {
                'meal': meal.name,
                'foods': [
                            {
                            'food': str(food.name),
                            'calories': str(food.calories),
                            'substitute': str(get_substitute(food)['substitute']),
                            'substitute_quantity': str(get_substitute(food)['quantity'])
                            }
                            for food in meal.foods.all()
                        ]
            
            } for meal in diet.meals.all()
            ] 
        }

        # json_str = json.dumps(diet_response)

        # # Write the JSON string to a file
        # with open('diet_response.json', 'w') as file:
        #     file.write(json_str)
        print(diet_response)


        return JsonResponse(diet_response, safe=False)

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
    
class addFood(APIView):
    def get(self, request, *args, **kwargs):
        request_patient = self.request.query_params.get('patient')
        form = FoodForm()

        return JsonResponse(form)
    
    def post(self, request, *args, **kwargs):
        request_patient = self.request.query_params.get('patient')
        form = FoodForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return JsonResponse(data, status=200)
        else:
            data = form.errors.as_json()
            return JsonResponse(data, status=400) 


class AdvicesListView(APIView):
    
    def get(self, request, *args, **kwargs):
        
        today = datetime.datetime.now().date()
        advices = Advice.objects.filter(is_active=True, expire_date__gte=today)
        results = [advice.to_json() for advice in advices]
        return JsonResponse(results, status=200, safe=False)
        
