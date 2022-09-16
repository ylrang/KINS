from django.contrib import admin
from .models import Tag, Docs, Document, Site, Keyword, SWFactor
# from import_export.admin import ImportExportModelAdmin
# from .resource import DocsResource

admin.site.register(Tag)
admin.site.register(Docs)
admin.site.register(Document)
admin.site.register(Keyword)
admin.site.register(Site)
admin.site.register(SWFactor)

# class DocsAdmin(ImportExportModelAdmin):
#     resource_class = DocsResource
#     list_display = ('title', 'serial_num', 'index_num', 'index_title')
#
#
# admin.site.register(Docs, DocsAdmin)
