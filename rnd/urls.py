from django.urls import path
# urls.py
from rnd import views, apis

app_name='rnd'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

    path('case', views.case, name='case'),
    path('KAERI_case', views.KAERI, name='KAERI_case'),
    path('KORAD_case', views.KORAD, name='KORAD_case'),
    path('create_case', views.create_case, name='create_case'),
    path('case_detail', views.case_detail, name='case_detail'),

    path('regulation', views.regulation, name='regulation'),
    path('regulation_detail<int:pk>', views.regulation_detail, name='regulation_detail'),
    path('download/<path:filename>', views.download_regulation_file, name='download_regulation_file'),

    path('institute', views.institute, name='institute'),
    
    path('api/regulation', apis.RegulationList.as_view(), name='regulation_api'),
    path('api/regulation/<int:pk>', apis.RegulationDetail.as_view(), name='regulation_detail_api'),
    path('api/case', apis.CaseList.as_view(), name='case_api'),
    path('api/case/<int:pk>', apis.CaseDetail.as_view(), name='case_detail_api'),
]