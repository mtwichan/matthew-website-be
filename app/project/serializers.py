from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "title",
            "slug",
            "preview_img",
            "created_on",
            "updated_on",
            "created",
            "description",
            "content",
            "status",
        ]