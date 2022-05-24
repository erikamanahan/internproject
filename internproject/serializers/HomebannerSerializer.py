from rest_framework import serializers
from internproject.models.HomeBanner import HomeBanner

__all__ = [ 'HomeBannerSerializer']


class HomeBannerSerializer(serializers.ModelSerializer):


    class Meta:
        model = HomeBanner
        fields = ('__all__')

