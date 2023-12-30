from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('trucks/<str:slug>/', views.TrucksDetailView.as_view(), name='trucks'),
]

