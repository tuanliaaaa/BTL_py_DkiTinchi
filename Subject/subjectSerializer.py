from wsgiref import validate
from django.forms import ValidationError

from rest_framework import serializers
from Subject.subjectModels import Subject
class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    SubjectCode = serializers.CharField(max_length=255)
    SubjectName = serializers.CharField(max_length=255)
    def create(self, validated_data):
        return Subject.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.SubjectCode = validated_data.get('SubjectCode', instance.SubjectCode)
        instance.SubjectName = validated_data.get('SubjectName', instance.SubjectName)
        instance.save()
        return instance