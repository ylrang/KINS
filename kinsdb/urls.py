from django.urls import path
# urls.py
from kinsdb import views


urlpatterns = [
    path('database-index', views.index, name='database-index'),
    path('institution', views.institution, name='institution'),
    path('database<str:company><str:institution>', views.database, name='database'),
    path('docs-details<int:pk>', views.docs_detail, name='docs-details'),
    path('download/<path:filename>', views.download_file, name='download_file'),
]
