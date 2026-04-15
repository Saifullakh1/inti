from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Like
from .serializers import CommentSerializer, LikeSerializer
from posts.models import Post
from users.models import User


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        post = request.data['post']
        user = request.data['user']
        like_obj = Like.objects.filter(post__id=post, user__id=user).first()
        if like_obj:
            like_obj.delete()
            return Response({"message": "deleted"}, status=status.HTTP_200_OK)
        else:
            post = Post.objects.filter(id=post).first()
            user = User.objects.filter(id=user).first()
            Like.objects.create(post=post, user=user)
        return Response({"message": "created"}, status=status.HTTP_201_CREATED)