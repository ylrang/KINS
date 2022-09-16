from django.urls import path
from kinsdb import views

urlpatterns = [
    path('database-index', views.index, name='database-index'),
    path('institution', views.institution, name='institution'),
    path('site', views.site, name='site'),
    path('database<str:_tag>', views.database, name='database'),
    path('database', views.database, name='database'),
    path('docs-details<int:pk>', views.docs_detail, name='docs-details'),
    path('site-details<int:pk>', views.site_detail, name='site-details'),
    path('download/<path:filename>', views.download_file, name='download_file'),
    path('unist', views.unist, name='unist'),
    path('safety', views.safety, name='safety'),
    path('detail-safety<str:doc>', views.detail_safety, name='detail-safety'),
    path('temp-safety<str:doc>', views.temp_safety, name='temp-safety'),
    path('kbs-3', views.kbs, name='kbs-3'),
    path('component<str:cmp>', views.component, name='component'),
    path('siting<str:country>', views.siting, name='siting'),
    path('details<str:country>_<str:title>', views.details, name='details'),
    path('details-component<str:title>', views.detail_component, name='details-component'),
    # path('upload', views.simple_upload, name='upload'),
]
