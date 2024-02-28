from django.urls import path
from . import views



urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    path('images/<str:filename>/', views.serve_uploaded_image),
]