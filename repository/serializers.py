from rest_framework import serializers
from .models import Project, Application, Resource

class ProjectSerializer(serializers.ModelSerializer):
    logicalId = serializers.UUIDField(source='logical_id', read_only=True)

    class Meta:
        model = Project
        fields = ['logicalId', 'name', 'description', 'type']
        read_only_fields = ['logicalId']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['logical_id', 'name', 'description']
        read_only_fields = ['logical_id']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['logical_id', 'name', 'uri']
        read_only_fields = ['logical_id']