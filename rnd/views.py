from django.shortcuts import render, redirect
from .models import Regulation, Case
import os
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from .forms import CaseForm
from django.utils import timezone

def index(request):
    return render(request, "rnd/index.html")

def case(request):
    return render(request, "rnd/case.html")

def KAERI(request):
    return render(request, "rnd/KAERI_case.html")

def KORAD(request):
    return render(request, "rnd/KORAD_case.html")

def create_case(request):
    if request.method == "POST":
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid:
            form.save(commit=False)
            form.creation_date = timezone.now()
            form.save()
            return redirect("rnd:index")
    else:
        form=CaseForm()
    return render(request, "rnd/create_case.html", {'form': form})

def case_detail(request, pk):
    case = Case.objects.get(pk=pk)
    context = {'case': case}
    return render(request, "rnd/case_detail.html", context)

def about(request):
    return render(request, "rnd/about.html")

def regulation(request):
    return render(request, "rnd/regulation.html")

def regulation_detail(request, pk):
    reg = Regulation.objects.get(pk=pk)
    context = {'reg': reg}
    return render(request, "rnd/regulation_detail.html", context)

def download_regulation_file(request, filename):
    file_path = os.path.abspath("media")
    file_name = os.path.basename(filename)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'r'),
                            content_type='application/force-download')  # mime_type
    response['Content-Disposition'] = 'attachment; filename=""'

    return response
def institute(request):
    return render(request, "rnd/institute.html")