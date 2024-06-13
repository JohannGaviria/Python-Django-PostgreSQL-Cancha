from rest_framework import serializers
from .models import SurfaceType, CourtStatus, CourtType, Court, CourtImage


class SurfaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfaceType
        fields = [
            'id',
            'type'
        ]


class CourtStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtStatus
        fields = [
            'id',
            'status'
        ]


class CourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtType
        fields = [
            'id',
            'type'
        ]


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = [
            'id',
            'name',
            'code',
            'size',
            'location',
            'price_hour',
            'description',
            'cover_image',
            'surface_type',
            'court_status',
            'court_type'
        ]


class CourtImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtImage
        fields = [
            'id',
            'image',
            'description',
            'court'
        ]
