from email import header
from rest_framework import serializers
from .models import NUser, csvfile,Table, rapport
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import base64
import pandas as pd


class csvfileSerialiser(serializers.ModelSerializer):
    class Meta:
        model=csvfile
        fields = '__all__'
      



class uploadcsvSerializer(serializers.Serializer):
    file=serializers.ImageField()
           

       
class searchSerializer(serializers.Serializer):
    data=serializers.CharField(max_length=200)
    msg_id=serializers.CharField(max_length=200)


class NUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = NUser
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = '__all__'


class CreatePdfSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = rapport
        fields = '__all__'





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['password'] = user.password
        token['last_name'] = user.last_name
        token['first_name'] = user.first_name
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name','is_superuser')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):


        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_superuser=validated_data['is_superuser'],


        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user