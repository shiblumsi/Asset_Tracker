from rest_framework import serializers
from .models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Users
        fields = ['email', 'name', 'password', 'password2']
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, data):
        pass1 = data.get('password')
        pass2 = data.get('password2')
        if pass1 != pass2:
            raise serializers.ValidationError('Password not match')
        return data

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = Users
        fields = ['email','password']




class AddEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name','phone','email','designation')


class AddAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class DelegateToSerializer(serializers.ModelSerializer):
    
    #assets = serializers.StringRelatedField(many=True, read_only=True)
    #employee = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = DelegateTo
        fields = ('employee','assets','checked_out_at','condition')


class WhenGiveAndReturnSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField( read_only=True)
    class Meta:
        model = GiveBack
        fields = ('asset_type','model','brand','checked_out_time','returned_date')


class ConditionGiveAndReturnSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = GiveBack
        fields = ('employee_name','asset_type','model','brand','delegate_condition','returned_condition')