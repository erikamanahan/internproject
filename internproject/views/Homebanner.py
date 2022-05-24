from internproject.models import HomeBanner
from rest_framework.views import APIView
from internproject.serializers import HomeBannerSerializer
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


__all__ = ['BannerHomeCreate','BannerHomeUpdate']

class BannerHomeCreate(ListCreateAPIView):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer

class BannerHomeUpdate(RetrieveUpdateDestroyAPIView):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer
