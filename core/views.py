from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FoodForm
from .models import *
import numpy as np
import traceback
from django.core.files.base import ContentFile
import base64
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

class LoginView(APIView):

    def get(request, *args, **kwargs):
        return render(request, 'login.html')

    def post(request, *args, **kwargs):

        template_name = 'login.html'

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('test'))
        else:
            return render(request, template_name, {
                'message': 'Invalid username and/or password.',
            })

class FoodListView(APIView):

    def get(request, *args, **kwargs):
        foods = Food.objects.all()

        for food in foods:
            food.image = food.get_images.first()

        return render(request, 'index.html', {
            'foods': foods,
            'title': 'Food List'
        })

class FoodDetailsView(APIView):

    def get(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        food_id = kwargs['food_id']
        food = Food.objects.get(id=food_id)

        return render(request, 'food.html', {
            'food': food,
            'images': food.get_images.all(),
        })
