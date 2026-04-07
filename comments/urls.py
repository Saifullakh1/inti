from django.urls import path
from .views import CommentAPIView, LikeAPIView


urlpatterns = [
    path('comments/', CommentAPIView.as_view(), name='comment'),
    path('likes/', LikeAPIView.as_view(), name='like'),
]