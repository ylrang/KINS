from django.urls import path
# urls.py
from cloud import views

urlpatterns = [

    #Cloud
    path('', views.CloudIndex.as_view(),name='index'),
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('notice', views.notice, name='notice'),


    # Jobs
    path('job-list', views.JobList.as_view(),name="job-list"),
    path('job-list-2', views.JobList2.as_view(),name="job-list-2"),
    path('job-grid', views.JobGrid.as_view(),name="job-grid"),
    path('job-grid-2', views.JobGrid2.as_view(),name="job-grid-2"),
    path('job-details', views.JobDetails.as_view(),name="job-details"),
    path('job-categories', views.JobCategories.as_view(),name="job-categories"),

    # Document Board
    path('shared-documents', views.SharedDocumentList.as_view(),name="shared-documents"),
    path('candidate-grid', views.CandidateGrid.as_view(),name="candidate-grid"),
    path('candidate-details', views.CandidateDetails.as_view(),name="candidate-details"),
    path('company-list', views.CompanyList.as_view(),name="company-list"),
    path('company-details', views.CompanyDetails.as_view(),name="company-details"),
    path('create-document', views.CreateDocument, name='create-document'),

    # Extra-Pages
    path('sign-up', views.SignUp.as_view(),name="sign-up"),
    path('sign-in', views.Signin.as_view(),name="sign-in"),
    path('sign-out', views.SignOut.as_view(),name="sign-out"),
    path('reset-password', views.ResetPassword.as_view(),name="reset-password"),
    path('comingsoon', views.ComingSoon.as_view(),name="comingsoon"),
    path('404-error', views.Error404.as_view(),name="404-error"),
    path('components', views.Components.as_view(),name="components"),

    path('Import_Excel_pandas/', views.Import_Excel_pandas, name='Import_Excel_pandas'),
    path('Import_excel', views.Import_excel, name='Import_excel'),

]

from jobcy import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
