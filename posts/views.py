from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, PostRetrieveSerializer


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # SELECT * FROM post
    serializer_class = PostSerializer # INSERT INTO post VALUES


class PostRetrieveAPView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() # SELECT * FROM post where id = 3
    serializer_class = PostSerializer # UPDATE post set where id = 3
                                        # DELETE FROM post where id = 3

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostRetrieveSerializer
        else:
            return self.serializer_class
