from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q, Avg
from .models import Patient, Food, PatientProgram, FoodSubstitute, Advice
from .forms import *
from .utils import *
import datetime

class DailyFoodView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
                
        try:
            patient = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            return JsonResponse({"error": "Paziente non trovato"}, status=status.HTTP_404_NOT_FOUND)
        
        diet_date = request.GET.get("date", None)
        
        response = []
        
        if diet_date:
        
            diet_date = datetime.datetime.strptime(diet_date, "%Y/%m/%d")
            today_date = datetime.datetime.now().date()
            patient_program = PatientProgram.objects.filter(Q(start_date__lte=today_date) & Q(end_date__gte=today_date), patient=patient, is_active=True).first()
            
            response = patient_program.get_date_meals(diet_date) if patient_program else []
            
        return JsonResponse(response, safe=False)

class DailyFoodListView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
                
        try:
            patient = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            return JsonResponse({"error": "Paziente non trovato"}, status=status.HTTP_404_NOT_FOUND)
        
        days_to_fetch = 10
        
        today_date = datetime.datetime.now().date()
        end_date = today_date + datetime.timedelta(days=days_to_fetch)
        patient_program = PatientProgram.objects.filter(Q(start_date__lte=today_date) & Q(end_date__gte=today_date), patient=patient, is_active=True).first()
        
        results = patient_program.get_ordered_meals(today_date, end_date) if patient_program else []
        
        return JsonResponse(results, safe=False)

class FoodDetailsView(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
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
    
class MealMicronutrientsView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        
        meal_id = kwargs.get("id")
        meal = Meal.objects.get(pk=meal_id)
        response = meal.get_micronutrients()
        return JsonResponse(response, safe=False) 
        
class WeightMeasureView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        
        patient = Patient.objects.get(user=request.user)
        weight_logs = WeightMeasure.objects.filter(patient=patient).order_by("entry_date")
        response = [ {"weight": weight_log.weight, "entry_date": weight_log.entry_date} for weight_log in weight_logs]
        
        return JsonResponse(response, safe=False)

    def post(self, request, *args, **kwargs):
        
        try:
            patient = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            return JsonResponse({"status_code": 404, "error": "Paziente non trovato"}, safe=False)
        
        try: 
            
            weight_log, cre = WeightMeasure.objects.get_or_create(patient=patient, entry_date=request.data["entry_date"])
            weight_log.patient = patient
            weight_log.weight = request.data["weight"]
            weight_log.entry_date = request.data["entry_date"]
            weight_log.save()
            
            return JsonResponse({"status_code": 200}, safe=False)
        
        except:
            import traceback
            traceback.print_exc()
            return JsonResponse({"status_code": 500}, safe=False)
        
class GetLogWeightData(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        
        patient = Patient.objects.get(user=request.user)
        current_year = datetime.datetime.now().year
        weight_logs = WeightMeasure.objects.filter(patient=patient, entry_date__year=current_year)
        result_data = {}
        monthly_avg = weight_logs.values('entry_date__month').annotate(avg_weight=Avg('weight'))

        for month_data in monthly_avg:
            month_number = month_data['entry_date__month'] - 1
            avg_weight = round(month_data['avg_weight'])
            result_data[month_number] = avg_weight
            
        return JsonResponse(result_data, safe=False)
           

class PatientView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        
        try:
            try:
                patient = Patient.objects.get(user=request.user)
            except Patient.DoesNotExist:
                return JsonResponse({"message": "Not found"}, safe=False, status=status.HTTP_404_NOT_FOUND)
            response = patient.to_json()
            return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
        except:
            import traceback
            traceback.print_exc()
            return JsonResponse({"message": "Generic error"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, *args, **kwargs):
        
        try:
            try:
                patient = Patient.objects.get(user=request.user)
            except Patient.DoesNotExist:
                return JsonResponse({"message": "Not found"}, safe=False, status=status.HTTP_404_NOT_FOUND)
                        
            patient.name = request.data['name'] if 'name' in request.data else patient.name
            patient.surname = request.data['surname'] if 'surname' in request.data else patient.surname
            patient.birth_date = datetime.datetime.strptime(request.data['birth_date'], "%d/%m/%Y") if 'birth_date' in request.data else patient.birth_date
            patient.email = request.data['email'] if 'email' in request.data else patient.email
            patient.phone_prefix = request.data['phone_prefix'] if 'phone_prefix' in request.data else patient.phone_prefix
            patient.phone = request.data['phone'] if 'phone' in request.data else patient.phone
            patient.height = request.data['height'] if 'height' in request.data else patient.height
            patient.weight = request.data['weight'] if 'weight' in request.data else patient.weight
            patient.gender = request.data['gender'] if 'gender' in request.data else patient.gender
            
            patient.save()
            
            return JsonResponse({"message": "ok"}, safe=False, status=status.HTTP_200_OK)
        except:
            import traceback
            traceback.print_exc()
            return JsonResponse({"message": "Generic error"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AdvicesListView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        
        today = datetime.datetime.now().date()
        advices = Advice.objects.filter(is_active=True, expire_date__gte=today)
        results = [advice.to_json() for advice in advices]
        return JsonResponse(results, status=200, safe=False)
        
