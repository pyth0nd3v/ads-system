from rest_framework import serializers
from ..models import Ad, Location

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["title", "visitors_per_day", "is_active"]


class LocationSerializer(serializers.ModelSerializer):
    ads = AdNameSerializer(many=True, read_only=True)
    class Meta:
        model = Location
        fields = ["keyword", "ads"]