from django.shortcuts import render

def database(request):
    return render(request, "kinsdb/database.html")
