from django.shortcuts import render
from kinsdb.models import Docs

def database(request):
    docs = Docs.objects.all()
    context = {'docs': docs}
    return render(request, "kinsdb/database.html", context)
