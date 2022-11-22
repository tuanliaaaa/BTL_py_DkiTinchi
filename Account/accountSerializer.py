
from wsgiref import validate
from pkg_resources import require
from rest_framework import serializers
from Account.accountModels import Account

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    status = serializers.IntegerField(required=False)
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('Password',None)
        return ret
    def validate(self, data):
        error=False
        try:
            account = Account.objects.get(username=data['username']) 
            error=True
        except:
            error= False
        finally:
            if(error):
                raise serializers.ValidationError("User đã tồn tại")
        return data
    def create(self, validated_data):
        return Account.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('Age', instance.password)
        instance.status = validated_data.get('Password', instance.status)
        instance.save()
        return instance