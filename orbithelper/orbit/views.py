from django.shortcuts import render
from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from django.http import JsonResponse


# Create your views here.

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        upload_folder = os.path.join(settings.STATIC_ROOT)
        os.makedirs(upload_folder, exist_ok=True)
        filename = os.path.join(upload_folder, image_file.name)
        with open(filename, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        image_url = os.path.relpath(filename, settings.STATIC_ROOT)
        return JsonResponse({'image_url': image_url})
    else:
        return JsonResponse({'error': 'No image uploaded or request method is not POST'})

def serve_uploaded_image(request, filename):
    image_path = os.path.join(settings.STATIC_ROOT,  filename)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            return HttpResponse(image_file.read(), content_type='image/jpg')  # Adjust content_type if needed
    else:
        return HttpResponse("Image not found", status=404)