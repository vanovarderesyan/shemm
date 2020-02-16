from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db import transaction
from rest_framework import serializers

from company.serializers import CompanySerializer
from task.serializers import TaskSerializer
from .models import (
    Client
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, required=False
    )

    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


# class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
#     # get_sr_price = serializers.SerializerMethodField('get_sr_price_func')
#
#     def get_sr_price_func(self, obj):
#         return self.context['request'].user  # access the request object
#
#     class Meta:
#         model = Organisation
#         fields = ('id', 'name', 'logo','client')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    # first_name = serializers.CharField(source='user.first_name')
    # last_name = serializers.CharField(source='user.last_name')
    # password = serializers.CharField(
    #     source='user.password',
    #     style={'input_type': 'password'},
    #     read_only=True
    # )

    # email = serializers.CharField(source='user.email')

    # state_many = StateLocalSerializer(many=True,read_only=True)
    client_company = CompanySerializer(many=True, read_only=True)
    client_task = TaskSerializer(many=True, read_only=True)

    user = UserSerializer()

    class Meta:
        model = Client
        fields = (
            'url',
            'id',
            'user',
            'client_company',
            'client_task',
            'user_id',
            'address',
            'phone',
            'image',
            'cover'
        )

    def create(self, validated_data):

        try:

            validated_data['user'] = User.objects.create(
                first_name=validated_data.get('user')['first_name'],
                last_name=validated_data.get('user')['last_name'],
                email=validated_data.get('user')['email'],
                password=make_password(validated_data.get('user')['password']),
                username=validated_data.get('user')['email']

            )

            # send_simple_message()

        except IntegrityError as e:
            raise serializers.ValidationError(e)

        instance = Client.objects.create(**validated_data)

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):

        print(validated_data.get('user')['first_name'])
        User.objects.filter(id=instance.user.id).update(first_name=validated_data.get('user')['first_name'],
                                                        last_name=validated_data.get('user')['last_name'])
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance
