from django.urls import path
from kinsdb import views

urlpatterns = [
    path('database-index', views.index, name='database-index'),
    path('institution', views.institution, name='institution'),
    path('site', views.site, name='site'),
    path('database<str:company>_<str:institution>', views.database, name='database'),
    path('docs-details<int:pk>', views.docs_detail, name='docs-details'),
    path('site-details<int:pk>', views.site_detail, name='site-details'),
    path('download/<path:filename>', views.download_file, name='download_file'),
    path('unist', views.unist, name='unist'),
]
