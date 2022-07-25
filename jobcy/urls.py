"""jobcy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# urls.py
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # Index Page
    path('', include('rnd.urls')),
    path('cloud', views.Index2.as_view(),name='index'),

    path('index-2/', views.Index2.as_view(),name='index-2'),
    path('index-3/', views.Index3.as_view(),name='index-3'),

    # Company
    path('company/',include('company.urls')),

    # Pages
    path('cloud/',include('cloud.urls')),

    # Blog
    path('blog/',include('blog.urls')),

    # Contact
    path('',include('contact.urls')),

    # Manage-Jobs
    path('manage-jobs',views.ManageJobs.as_view(),name='manage-jobs'),
    path('manage-jobs-post',views.ManageJobs.as_view(),name='manage-jobs-post'),
    path('bookmark-jobs',views.BookmarkJobs.as_view(),name='bookmark-jobs'),
    path('profile',views.Profile.as_view(),name='profile'),

    # Database
    path('kinsdb/',include('kinsdb.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
