from rest_framework import serializers
from .models import Post
from category.models import Category


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'created_at', 'category', 'category_name']
        extra_kwargs = {
            'image': {'required': False}
        }
