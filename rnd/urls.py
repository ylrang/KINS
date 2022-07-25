from django.urls import path
# urls.py
from rnd import views


urlpatterns = [
    path('', views.index, name='index'),
    path('support', views.support, name='support'),
    path('case', views.case, name='case'),
    path('about', views.about, name='about'),

]
