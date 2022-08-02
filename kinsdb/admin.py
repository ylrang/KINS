from django.contrib import admin
from .models import Tag, Docs, Document, Site, Keyword

admin.site.register(Tag)
admin.site.register(Docs)
admin.site.register(Document)
admin.site.register(Keyword)
admin.site.register(Site)
