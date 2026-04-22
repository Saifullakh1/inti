from rest_framework.response import Response
from rest_framework import generics
from .models import Post, Tag
from .serializers import (PostSerializer, PostRetrieveSerializer, TagSerializer,
                          TagRetrieveSerializer, PostCreateSerializer)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status



class TagAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagRetrieveSerializer


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # SELECT * FROM post
    serializer_class = PostSerializer # INSERT INTO post VALUES
    permission_classes = [AllowAny(), ]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), ]
        else:
            return self.permission_classes

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostRetrieveAPView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() # SELECT * FROM post where id = 3
    serializer_class = PostSerializer # UPDATE post set where id = 3
                                        # DELETE FROM post where id = 3

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostRetrieveSerializer
        else:
            return self.serializer_class
