from rest_framework import routers, serializers, viewsets
from .models import Villa


class VillaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villa
        fields = [
            'title',
            'image',
            'short_desc',
        ]


class VillaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villa
        fields = [
            'title',
            'image',
            'short_desc',
            'desc',
            'source'
        ]