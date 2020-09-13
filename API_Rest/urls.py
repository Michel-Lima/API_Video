from rest_framework import routers


from django.urls import path
from .api import VideoViewSet, Video_statistics

urlpatterns = [
    path('videos/', VideoViewSet.as_view()),
    path('statistics/', Video_statistics.as_view()),
]
