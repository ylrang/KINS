from import_export import resources
from .models import Docs


class DocsResource(resources.ModelResource):
    class meta:
        model = Docs
