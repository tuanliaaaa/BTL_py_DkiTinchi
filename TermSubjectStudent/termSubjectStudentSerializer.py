from wsgiref import validate
from django.forms import ValidationError
from rest_framework import serializers
from Term.termModels import Term
from Student.studentModels import Student
from SubjectMajor.subjectMajormodels import SubjectMajor
class TermSubjectStudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    student = serializers.CharField(max_length=255)
    term = serializers.CharField(max_length=255)
    subjectMajor = serializers.CharField(max_length=255)

    def to_internal_value(self, data):
        if 'student' in data:
            data['student']=Student.objects.get(pk=data['student'])
        if 'term' in data:
            data['term']=Term.objects.get(pk=data['term'])
        if 'subjectMajor' in data:
            data['subjectMajor']=SubjectMajor.objects.get(pk=data['subjectMajor'])
        return data
    def create(self, validated_data):
        return Term.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.student = validated_data.get('student', instance.student)
        instance.term = validated_data.get('term', instance.term)
        instance.subjectMajor = validated_data.get('subjectMajor', instance.subjectMajor)
        instance.save()
        return instance