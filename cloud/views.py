from django.views.generic import TemplateView


#Cloud
class CloudIndex(TemplateView):
    template_name = "cloud/index.html"


# Jobs
class JobList(TemplateView):
    template_name = "cloud/jobs/job-list.html"
class JobList2(TemplateView):
    template_name = "cloud/jobs/job-list-2.html"
class JobGrid(TemplateView):
    template_name = "cloud/jobs/job-grid.html"
class JobGrid2(TemplateView):
    template_name = "cloud/jobs/job-grid-2.html"
class JobDetails(TemplateView):
    template_name = "cloud/jobs/job-details.html"
class JobCategories(TemplateView):
    template_name = "cloud/jobs/job-categories.html"

# document-board
class SharedDocumentList(TemplateView):
    template_name = "cloud/document-board/shared-documents.html"
class CandidateGrid(TemplateView):
    template_name = "cloud/document-board/candidate-grid.html"
class CandidateDetails(TemplateView):
    template_name = "cloud/document-board/candidate-details.html"
class CompanyList(TemplateView):
    template_name = "cloud/document-board/company-list.html"
class CompanyDetails(TemplateView):
    template_name = "cloud/document-board/company-details.html"

# Extra-Pages
class SignUp(TemplateView):
    template_name = "cloud/extra-pages/sign-up.html"
class Signin(TemplateView):
    template_name = "cloud/extra-pages/sign-in.html"
class SignOut(TemplateView):
    template_name = "cloud/extra-pages/sign-out.html"
class ResetPassword(TemplateView):
    template_name = "cloud/extra-pages/reset-password.html"
class ComingSoon(TemplateView):
    template_name = "cloud/extra-cloud/coming-soon.html"
class Error404(TemplateView):
    template_name = "cloud/extra-pages/404-error.html"
class Components(TemplateView):
    template_name = "cloud/extra-pages/components.html"


from django.shortcuts import render

def notice(request):
    return render(request, "index/notice.html")

def CreateDocument(request):
    return render(request, "cloud/document-board/create_document.html")

def folder_list(request):
    return render(request, "cloud/bulletin/folder-list.html")

def folder_detail(request):
    return render(request, "cloud/bulletin/folder-detail.html")

def file_list(request):
    return render(request, "cloud/bulletin/file-list.html")

def file_detail(request):
    return render(request, "cloud/bulletin/file-detail.html")

def file_upload(request):
    return render(request, "cloud/bulletin/file-upload.html")

def file_update(request):
    return render(request, "cloud/bulletin/file-update.html")


from .models import *
# # from account.models import Folders
from .utils import Calendar
from datetime import timedelta
import calendar
from django.views import generic
from datetime import datetime, date
from django.utils.safestring import mark_safe

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cloud/extra-pages/cal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month





from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import Person


def Import_Excel_pandas(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        empexceldata = pd.read_excel(filename)
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Person.objects.create(code=dbframe.code, name=dbframe.name, phone=dbframe.phone, age=dbframe.age, grade=dbframe.grade)
            obj.save()

        return render(request, 'cloud/import_excel_db.html', {'uploaded_file_url': uploaded_file_url})

    return render(request, 'cloud/import_excel_db.html', {})


from tablib import Dataset
from .resource import PersonResource

def Import_excel(request):
    if request.method == 'POST' :
        Person =PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        data_import = dataset.load(new_person.read())

        result = PersonResource.import_data(dataset,dry_run=True)
        if not result.has_errors():
            PersonResource.import_data(dataset,dry_run=False)

        return render(request, 'cloud/import_excel_db.html', {} )
