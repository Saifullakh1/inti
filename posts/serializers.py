from rest_framework import serializers
from .models import Post, Tag
from comments.serializers import CommentSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class PostRetrieveSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True)
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
