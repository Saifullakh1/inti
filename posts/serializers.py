from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostRetrieveSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'likes', 'post_comments', 'created_at']

    def get_likes(self, obj):
        return obj.post_likes.count()