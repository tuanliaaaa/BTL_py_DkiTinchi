from wsgiref import validate
from django.forms import ValidationError
from Major.majorModels import Major
from Subject.subjectModels import Subject
from rest_framework import serializers
from SubjectMajor.subjectMajormodels import SubjectMajor
class SubjectMajorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    major = serializers.CharField(max_length=255)
    subject = serializers.CharField(max_length=255)
    numberOfCredits = serializers.IntegerField()
    startTerm = serializers.IntegerField()
    def to_internal_value(self, data):
        if 'subject' in data:
            data['subject']=Subject.objects.get(pk=data['Subject'])
        if 'major' in data:
            data['major']=Major.objects.get(pk=data['major'])
        return data
    def create(self, validated_data):
        return SubjectMajor.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.major = validated_data.get('major', instance.major)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.numberOfCredits = validated_data.get('numberOfCredits', instance.numberOfCredits)
        instance.startTerm = validated_data.get('startTerm', instance.startTerm)
        instance.save()
        return instance