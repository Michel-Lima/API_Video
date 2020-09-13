from rest_framework import routers


from django.urls import path
from .api import VideoViewSet, Video_statistics, Pagina_inicial

urlpatterns = [
    path('', Pagina_inicial),
    path('videos/', VideoViewSet.as_view(),name='videos'),
    path('statistics/', Video_statistics.as_view(),name='statistics'),
]
