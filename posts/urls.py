from django.urls import path
from .views import PostAPIView, PostRetrieveAPView, TagAPIView, TagRetrieveAPIView


urlpatterns = [
    path('', PostAPIView.as_view(), name='list'),
    path('<int:pk>', PostRetrieveAPView.as_view(), name='retrieve'),
    path('tags', TagAPIView.as_view(), name='list'),
    path('tags/<int:pk>', TagRetrieveAPIView.as_view(), name='retrieve')
]