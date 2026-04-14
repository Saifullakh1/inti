from django.urls import path
from .views import CommentAPIView, LikeAPIView, CommentRetrieveAPIView


urlpatterns = [
    path('comments/', CommentAPIView.as_view(), name='comment'),
    path('comments/<int:pk>', CommentRetrieveAPIView.as_view(), name='retrieve'),
    path('likes/', LikeAPIView.as_view(), name='like'),
]