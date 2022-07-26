from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "rnd/index.html")


def case(request):
    return render(request, "rnd/case.html")


def about(request):
    return render(request, "rnd/about.html")


def institute(request):
    return render(request, "rnd/institute.html")
