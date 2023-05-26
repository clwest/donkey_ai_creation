from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):

        posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
        
        class Meta:
          model = Post
          fields = ['id', 'user', 'title', 'content', 'image', 'caption', 'created_at', 'liked_by', 'disliked_by', 'updated_at', 'posts']