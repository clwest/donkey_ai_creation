from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post

class PostSerializer(serializers.ModelSerializer):

        posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
        
        class Meta:
          model = Post
          fields = ['id', 'user', 'title', 'content', 'image', 'caption', 'created_at', 'liked_by', 'disliked_by', 'updated_at', 'posts']
          
          
    # Use get_user_model to ensure we are referring to the correct user model
    # 
class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = get_user_model()
    fields = ('id', 'username',)