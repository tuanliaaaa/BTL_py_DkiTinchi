from wsgiref import validate
from django.forms import ValidationError
from Account.accountModels import Account
from rest_framework import serializers
from Teacher.teacherModels import Teacher
class AcountSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    fullName = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    account = serializers.CharField(max_length=255)
    def to_internal_value(self, data):
        if 'Account' in data:
            data['account']=Account.objects.get(pk=data['Account'])
        return data
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.fullName = validated_data.get('fullName', instance.fullName)
        instance.email = validated_data.get('email', instance.email)
        instance.account = validated_data.get('account', instance.account)
        instance.save()
        return instance