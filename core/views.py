from rest_framework.response import Response
from rest_framework.views import APIView
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


