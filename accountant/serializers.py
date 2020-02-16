from .models import (
    Accountant,Note
)
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from rest_framework.response import Response
from django.db import transaction

from django.core.mail import send_mail
import random
import string

import base64
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, required=False
    )

    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')



class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ('title', 'end_date', 'id','url','accountant')

class AccountantSerializer(serializers.HyperlinkedModelSerializer):
    # first_name = serializers.CharField(source='user.first_name')
    # last_name = serializers.CharField(source='user.last_name')
    # password = serializers.CharField(
    #     source='user.password',
    #     style={'input_type': 'password'},
    #     read_only=True
    # )

    # email = serializers.CharField(source='user.email')


    # state_many = StateLocalSerializer(many=True,read_only=True)

    user = UserSerializer()


    class Meta:
        model = Accountant
        fields = (
            'url',
            'id',
            'user',
            'user_id',
            'image',
            'phone'
        )

    def create(self, validated_data):

        try:

            validated_data['user'] = User.objects.create(
                first_name =  validated_data.get('user')['first_name'],
                last_name = validated_data.get('user')['last_name'],
                email=validated_data.get('user')['email'],
                password=make_password(validated_data.get('user')['password']),
                username =validated_data.get('user')['email']

            )

            # send_simple_message()

        except IntegrityError as e:
            raise serializers.ValidationError(e)

        instance = Accountant.objects.create(**validated_data)



        return instance



    @transaction.atomic
    def update(self, instance, validated_data):

        print(validated_data.get('user')['first_name'])
        User.objects.filter(id = instance.user.id).update(first_name=validated_data.get('user')['first_name'],
                                           last_name=validated_data.get('user')['last_name'],
                                           email=validated_data.get('user')['email'])
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance