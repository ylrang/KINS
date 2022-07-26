from django.urls import path
# urls.py
from rnd import views

app_name='rnd'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('case', views.case, name='case'),
    path('institute', views.institute, name='institute'),

]
