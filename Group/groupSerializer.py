from wsgiref import validate
from django.forms import ValidationError

from rest_framework import serializers
from Group.groupModels import Group
class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    groupName = serializers.CharField(max_length=255) 
    def create(self, validated_data):
        return Group.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.groupName = validated_data.get('groupName', instance.groupName)
        instance.save()
        return instance