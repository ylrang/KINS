from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index/index-1.html"
class CloudIndex(TemplateView):
    template_name = "cloud/index.html"
class Index3(TemplateView):
    template_name = "index/index-3.html"

# Manage-Jobs Page
class ManageJobs(TemplateView):
    template_name = "manage-jobs.html"
class ManageJobsPost(TemplateView):
    template_name = "manage-jobs-post.html"
class BookmarkJobs(TemplateView):
    template_name = "bookmark-jobs.html"
class Profile(TemplateView):
    template_name = "profile.html"
