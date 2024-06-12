"""
URLs for project app
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('SubmitRecording', views.SubmitRecording.as_view(), name="SubmitRecording"),
]