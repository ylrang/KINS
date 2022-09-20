from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "rnd/index.html")


def case(request):
    return render(request, "rnd/case.html")


def KAERI(request):
    return render(request, "rnd/KAERI_case.html")

def KORAD(request):
    return render(request, "rnd/KORAD_case.html")


def create_case(request):
    return render(request, "rnd/create_case.html")


def about(request):
    return render(request, "rnd/about.html")


def institute(request):
    return render(request, "rnd/institute.html")
