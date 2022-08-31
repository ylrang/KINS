from django.urls import path
from kinsdb import views

urlpatterns = [
    path('database-index', views.index, name='database-index'),
    path('institution', views.institution, name='institution'),
    path('site', views.site, name='site'),
    path('database<str:company>_<str:institution>_<str:_tag>', views.database, name='database'),
    path('database<str:company>_<str:institution>', views.database, name='database'),
    path('docs-details<int:pk>', views.docs_detail, name='docs-details'),
    path('site-details<int:pk>', views.site_detail, name='site-details'),
    path('download/<path:filename>', views.download_file, name='download_file'),
    path('unist', views.unist, name='unist'),
    path('safety', views.safety, name='safety'),
    path('kbs-3', views.kbs, name='kbs-3'),
    path('component<str:cmp>', views.component, name='component'),
    path('siting<str:country>', views.siting, name='siting'),
    path('sitings_details', views.ss, name='sitings_details'),

]
