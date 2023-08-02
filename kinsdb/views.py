from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
import os
from django.shortcuts import render
from kinsdb.models import Docs, Site, SWFactor, Document, Report, Issue, Data
from .filters import DocsFilter, SiteFilter
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count

from .resource import DocsResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


import pandas as pd

def analysis(request):
    qs = Docs.objects.all().values()
    data = pd.DataFrame(qs)
    context = {'df' : data.to_html() }

    return render(request, "kinsdb/Analysis/test.html", context)


# @api_view(['GET'])
# def wordcloud(request, doc_id):
#     doc = Docs.objects.get(id=doc_id)

from .forms import DataForm

def simple_upload(request):
    if request.method == 'POST':
        data = Data(
            document_id = request.POST['document'],
            file = request.FILES['file'],
        )
        # form.title =
        # docs_resource = DocsResource()
        # dataset = Dataset()
        if not data.file.name.endswith('csv'):
            messages.info(request, 'wrong format')
            return HttpResponse('잘못된 형식의 파일입니다.')
        else:
            data.save()
            return render(request, 'kinsdb/upload.html')
    else:
        form = DataForm
        context = {
            'form' : form,
        }
        return render(request, 'kinsdb/upload.html', context)


        # fs = FileSystemStorage(location='data', base_url='media/')
        # filename = fs.save(new_docs.name, new_docs)
        # uploaded_file_url = fs.url(filename)



        # imported_data = dataset.load(new_docs.read(), format='csv')
        # for data in imported_data:
        #     value = Docs(
        #         data[0],
        #         data[1],
        #         data[2],
        #         data[3],
        #     )
        #     value.save()

    return render(request, 'kinsdb/upload.html')



import csv
from django.db import IntegrityError

data = None

def upload_data(request):
    with open ('static/test_data_1.csv', 'r', encoding='cp949') as csv_file:
        count = 0
        rows = csv.DictReader(csv_file)
        uploaded = '업로드 완료 항목: '
        failed = '중복된 항목: '
        # next(rows, None)
        for row in rows:
            try:
                Docs.objects.create(
                    title = row['title'],
                    content_kor = row['content_kor'],
                    content_eng = row['content_eng'],
                    writer_id = row['writer'],
                    index_title_kor = row['index_title_kor'],
                    index_title_eng = row['index_title_eng'],
                    index_num = row['index_num'],
                    sector = row['sector'],
                    document_id = row['Document_ID'],
                )
                uploaded = uploaded + str(row['index_num']) + ', '
            except IntegrityError:
                count +=1
                failed = failed + str(row['index_num']) + ', '

            context = {'uploaded': uploaded, 'count': count , 'failed': failed}
    return render(request, 'kinsdb/Analysis/read_data.html', context)
    # return HttpResponse('중복인 데이터 ' + str(count) + '개를 제외한 항목이 업데이트 되었습니다.')/





def index(request):
    return render(request, "kinsdb/database-index.html")


def unist(request):
    return render(request, "kinsdb/UNIST/unist.html")



def report(request, report_num):
    rep = Report.objects.get(serial_num=report_num)
    issues = Issue.objects.select_related('report')
    context = {'rep': rep, 'issues': issues }
    return render(request, "kinsdb/UNIST/report.html", context)


def issue_detail(request, pk, report_num):
    issue = Issue.objects.get(id=pk)
    context = { 'issue': issue, 'report_num': report_num }
    return render(request, "kinsdb/UNIST/issue-detail.html", context)


def document(request, doc_num):
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

def brnc(request):
    return render(request, "kinsdb/BRNC/brnc.html")


def regulation_database(request):
    regulation_list = ['all','법률', '규정', '규제지침']
    docs = Docs.objects.all()
    search = request.GET.get('search', '')
    field = request.GET.get('field', '')
    country = request.GET.get('country', '')
    # sector = re/quest.GET.get('sector', '')
    documents = Document.objects.all()
    regulation = request.GET.getlist('regulation', regulation_list)

    docs = docs.filter(Q(title__icontains=search)).filter(Q(document__institution__icontains=country)).filter(Q(sector__icontains=field))
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
    return render(request, "kinsdb/BRNC/BRNC_database.html", context)


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



def wordcloud(request):
    content = Movie.objects.values('content')
    df = pd.DataFrame(content)
    BigdataPro.makeWordCloud(df.content)
    return render(request, 'bigdata_pro/wordcloud.html', {'content':df.content})
