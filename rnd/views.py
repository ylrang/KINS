from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "rnd/index.html")


def support(request):
    return render(request, "rnd/support.html")


def case(request):
    return render(request, "rnd/case.html")


def about(request):
    return render(request, "rnd/about.html")
