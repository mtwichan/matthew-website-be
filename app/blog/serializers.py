from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
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