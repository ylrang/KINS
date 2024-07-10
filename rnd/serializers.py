from rest_framework import serializers
from .models import Regulation, Case

class RegulationSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    creation_date = serializers.DateTimeField(required=True, format="%Y-%m-%d", input_formats=['iso-8601', '%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model = Regulation
        fields = ['pk', 'creation_date', 'title', 'description', 'writer', 'file']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        file = {
            "path" : representation.pop("file"),
            "name" : instance.file.name,
            "formatted_size" : file_size_format(instance.file)
        }
        representation['file'] = file
        return representation
        
class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['pk', 'creation_date', 'update_date', 'orgainzation', 'summary', 'file', 'writer']
        
        
def file_size_format(file):
    size = file.size
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return size, 'B'