from wsgiref import validate
from django.forms import ValidationError
from Account.accountModels import Account
from rest_framework import serializers
from Account.accountModels import Account
from Student.studentModels import Student
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    studentCode = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    account = serializers.CharField(max_length=255)
    fullName = serializers.CharField(max_length=255)
    def to_internal_value(self, data):
        if 'account' in data:
            data['account']=Account.objects.get(pk=data['account'])
        return data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.studentCode = validated_data.get('studentCode', instance.studentCode)
        instance.email = validated_data.get('email', instance.email)
        instance.account = validated_data.get('account', instance.account)
        instance.fullName = validated_data.get('fullName', instance.fullName)
        instance.save()
        return instance