from wsgiref import validate
from django.forms import ValidationError

from rest_framework import serializers
from Term.termModels import Term
class TermSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    termName = serializers.CharField(max_length=255)
    StartTimeSignTerm = serializers.DateTimeField()
    EndTimeSignTerm = serializers.DateTimeField()
    StartTimeSignSubject = serializers.DateTimeField()
    EndTimeSignSubject = serializers.DateTimeField()
   
    def create(self, validated_data):
        return Term.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.termName = validated_data.get('termName', instance.termName)
        instance.StartTimeSignTerm = validated_data.get('StartTimeSignTerm', instance.StartTimeSignTerm)
        instance.EndTimeSignTerm = validated_data.get('EndTimeSignTerm', instance.EndTimeSignTerm)
        instance.StartTimeSignSubject = validated_data.get('StartTimeSignSubject', instance.StartTimeSignSubject)
        instance.EndTimeSignSubject = validated_data.get('EndTimeSignSubject', instance.EndTimeSignSubject)
        instance.save()
        return instance