from wsgiref import validate
from django.forms import ValidationError
from SubjectMajor.subjectMajormodels import SubjectMajor
from Teacher.teacherModels import Teacher
from rest_framework import serializers
from sectionClass.sectionClassModels import sectionClass
class SectionClassSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    subjectMajor = serializers.CharField(max_length=255)
    teacherID = serializers.CharField(max_length=255)
    dayStart = serializers.DateField()
    quanlity = serializers.IntegerField()
    quanlityReal = serializers.IntegerField()
    dayDefault = serializers.CharField(max_length=255)
    dayAdd = serializers.CharField()
    dayLessonList = serializers.CharField()
    dayEnd = serializers.DateField()
    term =serializers.CharField(max_length=255)
    def to_internal_value(self, data):
        if 'subjectMajor' in data:
            data['subjectMajor']=SubjectMajor.objects.get(pk=data['subjectMajor'])
        if 'teacherID' in data:
            data['teacherID']=Teacher.objects.get(pk=data['teacherID'])
        if 'termMajorSubject' in data:
            data['termMajorSubject']=Teacher.objects.get(pk=data['termMajorSubject'])
        return data
    def create(self, validated_data):
        return sectionClass.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.subjectMajor = validated_data.get('subjectMajor', instance.subjectMajor)
        instance.teacherID = validated_data.get('teacherID', instance.teacherID)
        instance.dayStart = validated_data.get('dayStart', instance.dayStart)
        instance.quanlity = validated_data.get('quanlity', instance.quanlity)
        instance.quanlityReal = validated_data.get('quanlityReal', instance.quanlityReal)
        instance.dayDefault = validated_data.get('dayDefault', instance.dayDefault)
        instance.dayAdd = validated_data.get('dayAdd', instance.dayAdd)
        instance.dayLessonList = validated_data.get('dayLessonList', instance.dayLessonList)
        instance.dayEnd = validated_data.get('dayEnd', instance.dayEnd)
        instance.termMajorSubject = validated_data.get('termMajorSubject', instance.termMajorSubject)
        instance.save()
        return instance