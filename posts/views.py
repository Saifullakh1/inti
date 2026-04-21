from rest_framework import generics
from .models import Post, Tag
from .serializers import PostSerializer, PostRetrieveSerializer, TagSerializer, TagRetrieveSerializer
from rest_framework.permissions import IsAuthenticated


class TagAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagRetrieveSerializer


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # SELECT * FROM post
    serializer_class = PostSerializer # INSERT INTO post VALUES
    permission_classes = [IsAuthenticated, ]


class PostRetrieveAPView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() # SELECT * FROM post where id = 3
    serializer_class = PostSerializer # UPDATE post set where id = 3
                                        # DELETE FROM post where id = 3

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostRetrieveSerializer
        else:
            return self.serializer_class
