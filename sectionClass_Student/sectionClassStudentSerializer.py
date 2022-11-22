from wsgiref import validate
from django.forms import ValidationError
from Student.studentModels import Student
from sectionClass.sectionClassModels import sectionClass
from rest_framework import serializers
from sectionClass_StudentModels import sectionClassStudent
class SectionClassStudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    studentID = serializers.CharField(max_length=255)
    sectionClassID = serializers.CharField(max_length=255)
    def to_internal_value(self, data):
        if 'studentID' in data:
            data['studentID']=sectionClass.objects.get(pk=data['studentID'])
        if 'sectionClassID' in data:
            data['sectionClassID']=Student.objects.get(pk=data['sectionClassID'])
        return data
    def create(self, validated_data):
        return sectionClassStudent.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.studentID = validated_data.get('studentID', instance.studentID)
        instance.sectionClassID = validated_data.get('sectionClassID', instance.sectionClassID)
        instance.save()
        return instance