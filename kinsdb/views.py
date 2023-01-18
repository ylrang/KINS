from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
import os
from django.shortcuts import render
from kinsdb.models import Docs, Site, SWFactor, Document
from .filters import DocsFilter, SiteFilter
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count

from .resource import DocsResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def simple_upload(request):
    if request.method == 'POST':
        docs_resource = DocsResource()
        dataset = Dataset()
        new_docs = request.FILES['myfile']

        if not new_docs.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'kinsdb/upload.html')

        imported_data = dataset.load(new_docs.read(), format='xlsx')
        for data in imported_data:
            value = Docs(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()

    return render(request, 'kinsdb/upload.html')



def index(request):
    return render(request, "kinsdb/database-index.html")


def unist(request):
    return render(request, "kinsdb/UNIST/unist.html")


def document(request):
    return render(request, "kinsdb/UNIST/document.html")

def document_detail(request):
    return render(request, "kinsdb/UNIST/document-detail.html")

# 1


def safety(request):
    return render(request, "kinsdb/UNIST/safety-case.html")


def detail_safety(request, doc):
    context = {'doc': doc}
    return render(request, "kinsdb/UNIST/safety-detail.html", context)


def temp_safety(request, doc):
    context = {'doc': doc}
    return render(request, "kinsdb/UNIST/safety-temp.html", context)


# 2
def kbs(request):
    return render(request, "kinsdb/UNIST/kbs-3.html")


def component(request, cmp):
    context = {'cmp': cmp}
    return render(request, "kinsdb/UNIST/component-list.html", context)


def detail_component(request, title):
    context = {'title': title}
    return render(request, "kinsdb/UNIST/component-detail.html", context)


# 3
def siting(request, country):
    sites = Site.objects.filter(country=country)

    context = {'country': country, 'sites': sites}
    return render(request, "kinsdb/UNIST/siting.html", context)


def details(request, country, title):
    # if site.country = '스웨덴':
    #     factor = SWFactor.objects.filter(title=title)
    # else:
    # factors = SWFactor.objects.filter(title='지하수 조성')
    factors = SWFactor.objects.filter(title=title)
    context = {'site': site, 'country': country,
               'factors': factors, 'title': title}

    return render(request, "kinsdb/UNIST/siting-detail.html", context)


def brnc(request, _tag=''):
    regulation_list = ['all','법률', '규정', '규제지침']
    docs = Docs.objects.all()
    search = request.GET.get('search', '')
    field = request.GET.get('field', '')
    country = request.GET.get('country', '')
    documents = Document.objects.all()
    regulation = request.GET.getlist('regulation', regulation_list)

    docs = docs.filter(Q(title__icontains=search)).filter(Q(document__institution__icontains=country))
    # .filter(Q(field__in=field))

    # if field == 'title':
    #     docs = docs.filter(Q(title__icontains=search)).filter(
    #         Q(document__serial_num__icontains=document)).filter(Q(document__institution__in=country))
    # elif field == 'tag':
    #     docs = docs.filter(Q(tags__tag_content__icontains=search)).filter(Q(document__serial_num__icontains=document)).filter(Q(document__institution__in=country))

    # if _tag == '':
    #     tag = request.GET.get('tag', '')
    # else:
    #     tag = _tag
    #     docs = docs.filter(Q(tags__tag_content__icontains=tag))

    docsFilter = DocsFilter(request.GET, queryset=docs)
    docs = docsFilter.qs

    paginator = Paginator(docs, 5)
    page_number = request.GET.get('page', '1')
    page_obj = paginator.page(page_number)

    context = {'page_obj': page_obj, 'field': field, 'docsFilter': docsFilter,
               'search': search, 'documents': documents, 'country': country, 'regulation': regulation }
    return render(request, "kinsdb/BRNC_database.html", context)


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
    context = {'counts': counts}
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
    context = {'counts': counts}
    return render(request, "kinsdb/site.html", context)


def docs_detail(request, pk):
    doc = Docs.objects.get(pk=pk)
    context = {'doc': doc}
    return render(request, "kinsdb/docs-detail.html", context)


def site_detail(request, pk):
    doc = Site.objects.get(pk=pk)
    context = {'doc': doc}
    return render(request, "kinsdb/site-detail.html", context)


def download_file(request, filename):
    file_path = os.path.abspath("media")
    file_name = os.path.basename(filename)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(filename, 'r'),
                            content_type='application/force-download')  # mime_type
    response['Content-Disposition'] = 'attachment; filename=""'

    return response
