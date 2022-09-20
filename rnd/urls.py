from django.urls import path
# urls.py
from rnd import views

app_name='rnd'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

    path('case', views.case, name='case'),
    path('KAERI_case', views.KAERI, name='KAERI_case'),
    path('KORAD_case', views.KORAD, name='KORAD_case'),
    path('create_case', views.create_case, name='create_case'),

    path('institute', views.institute, name='institute'),

]
