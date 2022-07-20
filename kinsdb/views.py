from django.shortcuts import render
from kinsdb.models import Docs
from .filters import DocsFilter
from django.core.paginator import Paginator
from django.db.models import Q


def database(request):
    docs = Docs.objects.all()
    search = request.GET.get('search', '')
    field = request.GET.get('field', '')

    if search:
        if field == 'title':
            docs = docs.filter(Q(title__icontains=search))
        elif field == 'tag':
            docs = docs.filter(Q(tags__tag_content__icontains=search))

    docsFilter = DocsFilter(request.GET, queryset=docs)
    docs = docsFilter.qs

    paginator = Paginator(docs, 5)
    page_number = request.GET.get('page', '1')
    page_obj = paginator.page(page_number)

    context = {'docs': docs, 'page_obj': page_obj, 'field': field, 'search': search }
    return render(request, "kinsdb/database.html", context)


def docs_detail(request, pk):
    doc = Docs.objects.get(pk=pk)
    context = {'doc': doc}
    return render(request, "kinsdb/docs-detail.html", context)
