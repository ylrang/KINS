from django.urls import path
# urls.py
from kinsdb import views

urlpatterns = [
    path('database', views.database, name='database'),

]
