from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Post

class PostSerializer(serializers.ModelSerializer):


        
        class Meta:
          model = Post
          fields = ['id', 'user', 'title', 'content', 'image', 'caption', 'created_at', 'liked_by', 'disliked_by', 'updated_at', ]
          
          
    # Use get_user_model to ensure we are referring to the correct user model
    # 
class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = get_user_model()
    fields = ('id', 'username',)