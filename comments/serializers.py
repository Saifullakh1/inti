from rest_framework import serializers
from .models import Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentForPostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')

    class Meta:
        model = Comment
        fields = ['id', 'description', 'name']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'