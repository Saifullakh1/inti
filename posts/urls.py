from django.urls import path
from .views import PostAPIView, PostRetrieveAPView


urlpatterns = [
    path('', PostAPIView.as_view(), name='list'),
    path('<int:pk>', PostRetrieveAPView.as_view(), name='retrieve')
]