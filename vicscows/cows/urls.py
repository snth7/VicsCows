from django.urls import path
from .import views

urlpatterns = [
    path('cows/', views.cows, name="cows"),
    path('bull/', views.cows, name="bull"),
]