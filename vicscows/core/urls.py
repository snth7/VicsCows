from django.urls import path
from .import views

    #path de core
urlpatterns = [
    path('', views.home, name="home"),
]