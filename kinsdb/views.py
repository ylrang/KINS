from django.shortcuts import render
from kinsdb.models import Docs, Site
from .filters import DocsFilter, SiteFilter
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request, "kinsdb/database-index.html")


def database(request, company, institution):
    if company == 'BRNC':
        docs = Docs.objects.filter(writer__company=company).filter(document__institution=institution)
        search = request.POST.get('search','')
        tag = request.POST.get('tag','')
        field = request.POST.get('field')

        if field == 'title':
            docs = docs.filter(Q(title__icontains=search))
        elif field == 'tag':
            docs = docs.filter(Q(tags__tag_content__icontains=tag))


        docsFilter = DocsFilter(request.GET, queryset=docs)
        docs = docsFilter.qs

        paginator = Paginator(docs, 5)
        page_number = request.GET.get('page', '1')
        page_obj = paginator.page(page_number)

        context = {'page_obj': page_obj, 'field': field, 'tag': tag, 'docsFilter': docsFilter }
        return render(request, "kinsdb/%s_database.html" %company, context)

    elif company == 'UNIST':
        docs = Site.objects.filter(writer__company=company).filter(country=institution)
        search = request.GET.get('search','')
        key = request.GET.get('key','')
        field = request.GET.get('field')

        if field == 'title':
            docs = docs.filter(Q(title__icontains=search))
        elif field == 'key':
            docs = docs.filter(Q(keywords__key_content__icontains=key))

        siteFilter = SiteFilter(request.GET, queryset=docs)
        docs = siteFilter.qs

        paginator = Paginator(docs, 5)
        page_number = request.GET.get('page', '1')
        page_obj = paginator.page(page_number)

        context = { 'page_obj': page_obj, 'field': field, 'key': key, 'siteFilter': siteFilter }
        return render(request, "kinsdb/%s_database.html" %company, context)


def db(request, company, institution):
    docs = Site.objects.filter(writer__company=company).filter(country=institution)
    search = request.GET.get('search','')
    key = request.GET.get('key','')
    field = request.GET.get('field')

    if field == 'title':
        docs = docs.filter(Q(title__icontains=search))
    elif field == 'key':
        docs = docs.filter(Q(keywords__key_content__icontains=key))

    siteFilter = SiteFilter(request.GET, queryset=docs)
    docs = siteFilter.qs

    paginator = Paginator(docs, 5)
    page_number = request.GET.get('page', '1')
    page_obj = paginator.page(page_number)

    context = { 'page_obj': page_obj, 'field': field, 'key': key, 'siteFilter': siteFilter }
    return render(request, "kinsdb/%s_database.html" %company, context)




def institution(request):
    return render(request, "kinsdb/institution.html")


def site(request):
    return render(request, "kinsdb/site.html")


def docs_detail(request, pk):
    doc = Docs.objects.get(pk=pk)
    context = {'doc': doc}
    return render(request, "kinsdb/docs-detail.html", context)


def site_detail(request, pk):
    doc = Site.objects.get(pk=pk)
    context = {'doc': doc}
    return render(request, "kinsdb/site-detail.html", context)


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
