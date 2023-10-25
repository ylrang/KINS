from django.urls import path
from kinsdb import views

urlpatterns = [
    # path('institution', views.institution, name='institution'), #v1
    # path('site', views.site, name='site'), #v1
    # path('document<int:doc_num>', views.document, name='document'), #v1
    # path('document_detail', views.document_detail, name='document_detail'), #v1
    # path('safety', views.safety, name='safety'), #v1
    # path('detail-safety<str:doc>', views.detail_safety, name='detail-safety'), #v1
    # path('temp-safety<str:doc>', views.temp_safety, name='temp-safety'), #v1
    # path('kbs-3', views.kbs, name='kbs-3'),
    # path('component<str:cmp>', views.component, name='component'),
    # path('siting<str:country>', views.siting, name='siting'),
    # path('details<str:country>_<str:title>', views.details, name='details'),
    # path('details-component<str:title>',
    #      views.detail_component, name='details-component'),
    # path('site-details<int:pk>', views.site_detail, name='site-details'),



### database ###
    path('database-index', views.index, name='database-index'), # 데이터베이스 개요

    ### brnc ###
    path('brnc', views.brnc, name='brnc'), #brnc 데이터베이스 표
    path('regulation_database', views.regulation_database,
         name='regulation_database'), # brnc 데이터베이스 접속 리스트
         path('docs-details<int:pk>', views.docs_detail, name='docs-details'), # brnc 데이터 상세화면

    ### unist ###
    path('unist', views.unist, name='unist'), # unist 데이터베이스 표
    path('report<int:report_num>', views.report, name='report'), # unist 보고서 화면/issue list
    path('issue_detail<int:pk><int:report_num>',
         views.issue_detail, name='issue_detail'), # unist 이슈데이터 상세화면



    ### file upload ###
    path('download/<path:filename>', views.download_file, name='download_file'),

    path('upload', views.simple_upload, name='upload'),

    path('wordcloud', views.wordcloud, name='wordcloud'),
    path('analysis', views.analysis, name='analysis'),
    path('upload_data', views.upload_data, name='upload_data'),
    # path('wordcloudview', views.WordCloudView, name='wordcloudview'),

]
