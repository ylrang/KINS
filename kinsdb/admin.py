from django.contrib import admin
from .models import Tag, Docs, Document, Site, Keyword, SWFactor, Report
from import_export.admin import ImportExportModelAdmin
from .resource import DocsResource

admin.site.register(Tag)
# admin.site.register(Docs)
admin.site.register(Document)
admin.site.register(Keyword)
admin.site.register(Site)
admin.site.register(SWFactor)
admin.site.register(Report)

# admin.site.register(Field)

class DocsAdmin(ImportExportModelAdmin):
    resource_class = DocsResource
    list_display = ('title', 'index_num')


admin.site.register(Docs, DocsAdmin)
