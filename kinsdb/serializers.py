from rest_framework import serializers
from .models import Docs

class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = ('id', 'title', 'content_kor', 'content_eng', 'regist_date', 'last_updated', 'writer', 'tags', 'views', 'index_title_kor', 'index_num', 'index_title_eng', 'sector', 'document', 'wc')

