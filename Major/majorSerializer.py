from wsgiref import validate
from django.forms import ValidationError

from rest_framework import serializers
from Major.majorModels import Major
class MajorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    majorName = serializers.CharField(max_length=255)
    majorCode = serializers.CharField(max_length=255)
    def create(self, validated_data):
        return Major.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.majorName = validated_data.get('majorName', instance.username)
        instance.majorCode = validated_data.get('majorCode', instance.status)
        instance.save()
        return instance