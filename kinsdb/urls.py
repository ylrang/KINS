from django.urls import path
# urls.py
from kinsdb import views

urlpatterns = [
    path('database-index', views.index, name='database-index'),
    path('database<str:company>', views.database, name='database'),
    path('docs-details<int:pk>', views.docs_detail, name='docs-details'),
]
