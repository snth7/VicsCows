from django.shortcuts import render, redirect

def cows(request):
    return render(request, "cows/cows.html")

def bull(request):
    return render(request, "cows/bull.html")