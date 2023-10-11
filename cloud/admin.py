from django.contrib import admin
from .models import Event, Person, Log, Files, Post

admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Log)
admin.site.register(Files)
admin.site.register(Post)
