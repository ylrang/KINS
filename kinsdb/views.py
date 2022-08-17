from django.shortcuts import render
from kinsdb.models import Docs, Site
from .filters import DocsFilter, SiteFilter
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count

def index(request):
    return render(request, "kinsdb/database-index.html")


def database(request, company, institution):
    if company == 'BRNC':
        docs = Docs.objects.filter(writer__company=company).filter(document__institution=institution)
        search = request.GET.get('search','')
        tag = request.GET.get('tag','')
        field = request.GET.get('field')

        if field == 'title':
            docs = docs.filter(Q(title__icontains=search))
        elif field == 'tag':
            docs = docs.filter(Q(tags__tag_content__icontains=search))


        docsFilter = DocsFilter(request.GET, queryset=docs)
        docs = docsFilter.qs

        paginator = Paginator(docs, 5)
        page_number = request.GET.get('page', '1')
        page_obj = paginator.page(page_number)

        context = {'page_obj': page_obj, 'field': field, 'tag': tag, 'docsFilter': docsFilter, 'search': search }
        return render(request, "kinsdb/%s_database.html" %company, context)

    elif company == 'UNIST':
        docs = Site.objects.filter(writer__company=company).filter(country=institution)
        search = request.GET.get('search','')
        key = request.GET.get('key','')
        field = request.GET.get('field')

        if field == 'title':
            docs = docs.filter(Q(title__icontains=search))
        elif field == 'key':
            docs = docs.filter(Q(keywords__key_content__icontains=search))

        siteFilter = SiteFilter(request.GET, queryset=docs)
        docs = siteFilter.qs

        paginator = Paginator(docs, 5)
        page_number = request.GET.get('page', '1')
        page_obj = paginator.page(page_number)

        context = { 'page_obj': page_obj, 'field': field, 'key': key, 'siteFilter': siteFilter, 'search':search }
        return render(request, "kinsdb/%s_database.html" %company, context)




def institution(request):
    # countries = Document.objects.all().values_list('institution', flat=True)
    ie = Docs.objects.filter(document__institution='IAEA').count()
    am = Docs.objects.filter(document__institution='미국').count()
    sw = Docs.objects.filter(document__institution='스웨덴').count()
    fn = Docs.objects.filter(document__institution='핀란드').count()
    fr = Docs.objects.filter(document__institution='프랑스').count()
    gm = Docs.objects.filter(document__institution='독일').count()
    ca = Docs.objects.filter(document__institution='캐나다').count()
    ja = Docs.objects.filter(document__institution='일본').count()
    counts = [ie, am, sw, fn, fr, gm, ca, ja]
    context = { 'counts': counts }
    return render(request, "kinsdb/institution.html", context)


def site(request):
    ie = Site.objects.filter(country='IAEA').count()
    am = Site.objects.filter(country='미국').count()
    sw = Site.objects.filter(country='스웨덴').count()
    fn = Site.objects.filter(country='핀란드').count()
    fr = Site.objects.filter(country='프랑스').count()
    gm = Site.objects.filter(country='독일').count()
    ca = Site.objects.filter(country='캐나다').count()
    ja = Site.objects.filter(country='일본').count()
    counts = [ie, am, sw, fn, fr, gm, ca, ja]
    context = { 'counts': counts }
    return render(request, "kinsdb/site.html", context)


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
