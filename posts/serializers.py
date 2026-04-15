from rest_framework import serializers
from .models import Post, Tag
from comments.serializers import CommentForPostSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    author = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'likes', 'created_at', 'tags', 'author']

    def get_likes(self, obj):
        return obj.post_likes.count()


class PostRetrieveSerializer(serializers.ModelSerializer):
    post_comments = CommentForPostSerializer(many=True)
    likes = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'likes', 'post_comments', 'created_at', 'tags']

    def get_likes(self, obj):
        return obj.post_likes.count()


class TagRetrieveSerializer(serializers.ModelSerializer):
    post_tags = PostSerializer(many=True)

    class Meta:
        model = Tag
        fields = ['id', 'title', 'post_tags']
