from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class LoginResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == 'POST' and request.path == '/api/v1/rest-auth/login/' and response.status_code == 200:
            user = request.user
            response.data['id'] = user.pk
            response.data['isSuperuser'] = user.is_superuser
            response.data['isStaff'] = user.is_staff
            response.data['isReader'] = not user.is_superuser and not user.is_staff
            response.data['username'] = user.username
            response.data['firstName'] = user.first_name
            response.data['lastName'] = user.last_name
            response.data['email'] = user.email
            return JsonResponse(response.data)
        return response