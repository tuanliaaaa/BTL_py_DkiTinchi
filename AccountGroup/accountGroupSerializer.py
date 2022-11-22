from wsgiref import validate
from django.forms import ValidationError
from rest_framework import serializers
from AccountGroup.accountGroupModels import AccountGroup
from Account.accountModels import Account
from Group.groupModels import Group
class AcountGroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    account = serializers.CharField(max_length=200)
    group = serializers.CharField(max_length=200)
    def to_internal_value(self, data):
        if 'group' in data:
            data['group']=Group.objects.get(pk=data['group'])
        if 'Category' in data:
            data['account']=Account.objects.get(pk=data['account'])
        return data
    def create(self, validated_data):
        return AccountGroup.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.account = validated_data.get('account', instance.account)
        instance.group = validated_data.get('group', instance.group)
        instance.save()
        return instance