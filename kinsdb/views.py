from django.shortcuts import render
from kinsdb.models import Docs
from .filters import DocsFilter
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request, "kinsdb/database-index.html")


def database(request, company, institution):
    docs = Docs.objects.filter(writer__company=company).filter(document__institution=institution)
    search = request.POST.get('search','')
    tag = request.POST.get('tag','')
    field = request.POST.get('field')

    if field == 'title':
        docs = docs.filter(Q(title__icontains=search))
    elif field == 'tag':
        docs = docs.filter(Q(tags__tag_content__icontains=tag))


    docsFilter = DocsFilter(request.POST, queryset=docs)
    docs = docsFilter.qs

    paginator = Paginator(docs, 5)
    page_number = request.POST.get('page', '1')
    page_obj = paginator.page(page_number)

    context = {'docs': docs, 'page_obj': page_obj, 'field': field, 'search': search, 'tag': tag }
    return render(request, "kinsdb/%s_database.html" %company, context)



def institution(request):
    return render(request, "kinsdb/institution.html")


def site(request):
    return render(request, "kinsdb/site.html")


def docs_detail(request, pk):
    doc = Docs.objects.get(pk=pk)
    context = {'doc': doc}
    return render(request, "kinsdb/docs-detail.html", context)


import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage


def download_file(request, filename):
    file_path = os.path.abspath("media")
    file_name = os.path.basename(filename)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(filename, 'r'),
                            content_type='application/force-download')  # mime_type
    response['Content-Disposition'] = 'attachment; filename=""'

    return response
