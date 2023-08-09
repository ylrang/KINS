from django.core.files.base import ContentFile
import urllib
import io
import base64
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from krwordrank.word import summarize_with_keywords
from .forms import DataForm
from konlpy.tag import Okt
from django.db import IntegrityError
import csv
from jobcy.settings import STATIC_ROOT
from collections import Counter
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
    context = {'df': data.to_html()}

    return render(request, "kinsdb/Analysis/test.html", context)


# from kinsdb.utils import read_file_by_file_extension, show_wordcloud
# def WordCloudView(request):
#     def get_context_data(self) -> dict[str, Any]:
#         """For storing our context."""
#         context: dict[str, Any] = {}
#         context["DataForm"] = DataForm()
#         return context
#     def narration_chart_data(self, request: HttpRequest, data:
#                             Optional[pd.DataFrame]) -> HttpResponse:
#         """For displaying wordcloud."""
#         context = self.get_context_data()
#         wordcloud = show_wordcloud(data)
#         context["wordcloud"] = wordcloud
#         return render(request, self.template_name, context)
#     def get(self, request: HttpRequest) -> HttpResponse:
#         return render(request,self.template_name,
#                      self.get_context_data())
#     def post(self, request: HttpRequest) -> HttpResponse:
#         context = self.get_context_data()
#         form = DataForm(request.POST, request.FILES)
#         values: list[str] = []
#         if form.is_valid():
#             user_file = form.cleaned_data["file"]
#             read_file = read_file_by_file_extension(user_file)
#             if read_file is not None:
#                 for _, row in read_file.iterrows():
#                     values.append(row["narration"])
#                 converted_to_string = " ".join(values)
#                 return self.narration_chart_data(request,
#                               converted_to_string)
#         else:
#             form = DataForm()
#         return render(request, "kinsdb/wordcloudvisualization.html", context)


def simple_upload(request):
    if request.method == 'POST':
        data = Data(
            document_id=request.POST['document'],
            file=request.FILES['file'],
        )
        # form.title =
        # docs_resource = DocsResource()
        # dataset = Dataset()
        if not data.file.name.endswith('csv'):
            messages.info(request, 'wrong format')
            return HttpResponse('잘못된 형식의 파일입니다.')
        else:
            data.save()
            return render(request, 'kinsdb/upload_data.html')
    else:
        form = DataForm
        context = {
            'form': form,
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


data = None


def wordcloud(content):
    okt = Okt()
    nouns = okt.nouns(content)

    words = [n for n in nouns if len(n) > 1]

    c = Counter(words)

    wc = WordCloud(width=400, height=400, scale=2.0, max_font_size=250,
                   font_path='/usr/share/fonts/truetype/nanum/NanumSquareB.ttf')
    gen = wc.generate_from_frequencies(c)
    plt.figure()

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')

    image = io.BytesIO()
    plt.savefig(image, format='png')

    image.seek(0)
    string = base64.b64encode(image.read())

    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    return image_64

    # wc.to_file(filename="wc_1.png")
    # # gen.to_file('media/images/data/test.png')
    #
    # context = {'c': c, 'words': words, 'wc': wc, 'gen': gen}
    #
    # return gen

from django.core.files.base import ContentFile
def upload_data(request):
    with open('static/test_data_1.csv', 'r', encoding='cp949') as csv_file:
        count = 0
        rows = csv.DictReader(csv_file)
        uploaded = '업로드 완료 항목: '
        failed = '중복된 항목: '
        # wc = wordcloud(
        #     '국제기본안전기준(International Basic Safety Standards)과 기타 기준[3, 13,14]에서 요구한 차등접근법에 따라, 폐기물을 보관하고 인간과 환경으로부터 격리하기 위해 선택된 처분체계의 능력은 해당 폐기물의 잠재적 위험에 상응한다. 본 간행물에서 명시한 요건은 모든 종류의 처분시설에 적용된다. 그러나 해당 요건을 충족하기 위해 필요한 대책마련의 범위는 차등접근에 따라 차이가 있을 수 있다. 이러한 점은 1.14 에서 언급한 다른 종류의 시설을 위한 안전지침에 반영된다. ')

        # next(rows, None)
        for row in rows:

            # format, imgstr = wc.split(';base64,')
            # ext = format.split('/')[-1]
            #
            # data = ContentFile(base64.b64decode(imgstr))

            # img = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

            try:
                wc_uri = wordcloud(row['content_kor'])
                Docs.objects.create(
                    title=row['title'],
                    content_kor=row['content_kor'],
                    content_eng=row['content_eng'],
                    writer_id=row['writer'],
                    index_title_kor=row['index_title_kor'],
                    index_title_eng=row['index_title_eng'],
                    index_num=row['index_num'],
                    sector=row['sector'],
                    document_id=row['Document_ID'],
                    wc=wc_uri,
                )
                uploaded = uploaded + str(row['index_num']) + ', '
            except IntegrityError:
                count += 1
                failed = failed + str(row['index_num']) + ', '

    context = {'uploaded': uploaded,
               'count': count, 'failed': failed, 'wc': wc_uri}
    return render(request, 'kinsdb/Analysis/read_data.html', context)

    # return HttpResponse('중복인 데이터 ' + str(count) + '개를 제외한 항목이 업데이트 되었습니다.')/

    # okt = Okt()
    # nouns = okt.nouns(content)
    #
    # words = [n for n in nouns if len(n) > 1]
    #
    # c = Counter(words)
    #
    # wc = WordCloud(width=400, height=400, scale=2.0, max_font_size=250, font_path='/usr/share/fonts/truetype/nanum/NanumSquareB.ttf')
    # gen = wc.generate_from_frequencies(c)
    # plt.figure()


def index(request):
    return render(request, "kinsdb/database-index.html")


def unist(request):
    return render(request, "kinsdb/UNIST/unist.html")


def report(request, report_num):
    rep = Report.objects.get(serial_num=report_num)
    issues = Issue.objects.select_related('report')
    context = {'rep': rep, 'issues': issues}
    return render(request, "kinsdb/UNIST/report.html", context)


def issue_detail(request, pk, report_num):
    issue = Issue.objects.get(id=pk)
    context = {'issue': issue, 'report_num': report_num}
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
    regulation_list = ['all', '법률', '규정', '규제지침']
    docs = Docs.objects.all()
    search = request.GET.get('search', '')
    field = request.GET.get('field', '')
    country = request.GET.get('country', '')
    # sector = re/quest.GET.get('sector', '')
    documents = Document.objects.all()
    regulation = request.GET.getlist('regulation', regulation_list)

    docs = docs.filter(Q(title__icontains=search)).filter(
        Q(document__institution__icontains=country)).filter(Q(sector__icontains=field))
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
               'search': search, 'documents': documents, 'country': country, 'regulation': regulation}
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


# def wordcloud(request):
#     content = Movie.objects.values('content')
#     df = pd.DataFrame(content)
#     BigdataPro.makeWordCloud(df.content)
#     return render(request, 'bigdata_pro/wordcloud.html', {'content':df.content})
