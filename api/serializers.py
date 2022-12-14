from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalInfo
        fields=('id','fullname','emailid','date_of_birth','gender','about')

class SignUpSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=10)
    password=serializers.CharField(max_length=10)
    confirm_password = serializers.CharField(max_length = 10)
    class Meta:
        model=UserSignUp
        fields=('username','password','confirm_password')
    def create(self,validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self,value):

        if value.get('password') != value.get('confirm_password'):
            raise serializers.ValidationError('Both the passwords does not match')
        return value

class SignUpOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpOtp
        fields = ('id','otp')
                