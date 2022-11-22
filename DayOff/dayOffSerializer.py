from wsgiref import validate
from django.forms import ValidationError

from rest_framework import serializers
from DayOff.dayOffModels import DayOff
class DayOffSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    dayOff = serializers.DateField()
    def create(self, validated_data):
        return DayOff.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.dayOff=validated_data.get('dayOff',instance.dayOff)
        instance.save()
        return instance