from django.shortcuts import render
from kinsdb.models import Docs
from .filters import DocsFilter
from django.core.paginator import Paginator
from django.db.models import Q


def database(request):
    docs = Docs.objects.all()
    search = request.GET.get('search', '')

    if search:
        docs = docs.filter(Q(title__icontains=search))

    myFilter = DocsFilter(request.GET, queryset=docs)
    docs = myFilter.qs

    paginator = Paginator(docs, 5)
    page_number = request.GET.get('page', '1')
    page_obj = paginator.page(page_number)

    print('HI')
    print(paginator)
    print(page_number)

    context = {'docs': docs, 'page_obj': page_obj }
    return render(request, "kinsdb/database.html", context)


def docs_detail(request):
    docs = Docs.objects.all()
    context = {'docs': docs}
    return render(request, "kinsdb/database.html", context)
