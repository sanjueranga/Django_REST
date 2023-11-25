from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

# Create your views here.
def get_all(request):
    posts= Post.objects.all()
    data = [{"id":post.id,"title": post.title, "content":post.content,"user":post.user.first_name} for post in posts]
    return JsonResponse({"users": data})



@csrf_exempt
def create_post(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        title = data.get('title')
        content = data.get('content')
        user_id = data.get('user_id')
        user = get_object_or_404(User, id=user_id)
        if not title or not user_id:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        post = Post.objects.create(title=title, content=content,user=user)
        return JsonResponse({'message': 'Post created successfully'})
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
       
        return JsonResponse({'error': f'Error creating post: {str(e)}'}, status=500)
