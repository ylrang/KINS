from django.shortcuts import render
from kinsdb.models import Docs
from .filters import DocsFilter
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request, "kinsdb/database-index.html")


def database(request, company):
    docs = Docs.objects.filter(writer__company=company)
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


def docs_detail(request, pk):
    doc = Docs.objects.get(pk=pk)
    context = {'doc': doc}
    return render(request, "kinsdb/docs-detail.html", context)
