from django.shortcuts import render
from .models import Regulation
import os
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse


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

def case_detail(request):
    return render(request, "rnd/case_detail.html")


def about(request):
    return render(request, "rnd/about.html")


def regulation(request):
    reg_list = Regulation.objects.all()
    context = {'reg_list': reg_list}

    return render(request, "rnd/regulation.html", context)

def regulation_detail(request, pk):
    reg = Regulation.objects.get(pk=pk)
    context = {'reg': reg}

    return render(request, "rnd/regulation_detail.html", context)


def download_regulation_file(request, filename):
    file_path = os.path.abspath("media")
    file_name = os.path.basename(filename)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(filename, 'r'),
                            content_type='application/force-download')  # mime_type
    response['Content-Disposition'] = 'attachment; filename=""'

    return response



def institute(request):
    return render(request, "rnd/institute.html")
