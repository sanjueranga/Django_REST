from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json



def say_hello_user(request):
    return HttpResponse("user saying Hello!")



def get_all(request):
    users = User.objects.all()
    data = [{"first_name": user.first_name, "last_name": user.last_name} for user in users]
    return JsonResponse({"users": data})

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            first_name = data.get('first_name')
            last_name = data.get('last_name')

            if not first_name or not last_name:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            user = User.objects.create(first_name=first_name, last_name=last_name)

            return JsonResponse({'message': 'User created successfully'})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error creating user: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})