from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('upload/', views.upload_audio, name='upload_audio'),
    path('audio/<int:pk>/', views.audio_detail, name='audio_detail'),
    path('transcript/<int:pk>/', views.transcript, name='transcript'),
]
