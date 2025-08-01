from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'stars', 'comment', 'post', 'post_title']
