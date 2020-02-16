from .models import (
    Repeated,
    Task,
    File,
    SMS
)
from rest_framework import serializers
from manager.serializers import ManagerSerializer
from accountant.serializers import AccountantSerializer
from client.models import Client
from accountant.models import Accountant
from manager.models import Manager

from django.contrib.auth.models import User

from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from rest_framework.response import Response


class FileSerializer(serializers.HyperlinkedModelSerializer):
    # get_sr_price = serializers.SerializerMethodField('get_sr_price_func')
    class Meta:
        model = File
        fields = ('id', 'file', 'url', 'task')


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name')


class MyClientSerializer(serializers.HyperlinkedModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'image', 'phone', 'user', 'url')


class MyAccountantSerializer(serializers.HyperlinkedModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Accountant
        fields = ('id', 'image', 'phone', 'user', 'url')


class MyManagerSerializer(serializers.HyperlinkedModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Manager
        fields = ('id', 'image', 'phone', 'user', 'url')


class SMSLocalSerializer(serializers.HyperlinkedModelSerializer):
    accountant = MyAccountantSerializer(read_only=True)
    manager = MyManagerSerializer(read_only=True)
    client = MyClientSerializer(read_only=True)

    class Meta:
        model = SMS
        fields = ('id', 'text', 'task', 'file', 'manager',
                  'accountant', 'client', 'url', 'created_date')


class SMSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SMS
        fields = ('id', 'text', 'task', 'file', 'manager',
                  'accountant', 'client', 'url', 'created_date')


class RepeatedSerializer(serializers.HyperlinkedModelSerializer):
    # get_sr_price = serializers.SerializerMethodField('get_sr_price_func')
    created_date = serializers.DateTimeField(read_only=True)

    client_first_name = serializers.CharField(
        source='company.client.user.first_name', read_only=True)
    client_last_name = serializers.CharField(
        source='company.client.user.last_name', read_only=True)
    client_image = serializers.ImageField(
        source='company.client.image', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_id = serializers.CharField(source='company.id', read_only=True)

    accountant_first_name = serializers.CharField(
        source='accountant.user.first_name', read_only=True)
    accountant_last_name = serializers.CharField(
        source='accountant.user.last_name', read_only=True)
    accountant_image = serializers.ImageField(
        source='accountant.image', read_only=True)

    is_active = serializers.BooleanField(required=False)

    class Meta:
        model = Repeated
        fields = (
            'id',
            'name',
            'company',
            'company_id',
            'client',
            'client_first_name',
            'client_last_name',
            'client_image',
            'company_name',
            'title',
            'text',
            'is_active',
            'duration',
            'accountant',
            'accountant_first_name',
            'accountant_last_name',
            'accountant_image',
            'manager',
            'repeated_type',
            'repeated_value',
            'url',
            'created_date')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # get_sr_price = serializers.SerializerMethodField('get_sr_price_func')
    task_file = FileSerializer(many=True, read_only=True)
    sms_task = SMSLocalSerializer(many=True, read_only=True)
    created_date = serializers.DateTimeField(read_only=True)

    client_first_name = serializers.CharField(
        source='company.client.user.first_name', read_only=True)
    client_last_name = serializers.CharField(
        source='company.client.user.last_name', read_only=True)
    client_image = serializers.ImageField(
        source='company.client.image', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_id = serializers.CharField(source='company.id', read_only=True)

    accountant_first_name = serializers.CharField(
        source='accountant.user.first_name', read_only=True)
    accountant_last_name = serializers.CharField(
        source='accountant.user.last_name', read_only=True)
    accountant_image = serializers.ImageField(
        source='accountant.image', read_only=True)

    is_archive = serializers.BooleanField(required=False)
    is_repeated = serializers.BooleanField(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'company',
            'company_id',
            'client',
            'client_first_name',
            'client_last_name',
            'client_image',
            'company_name',
            'status',
            'title',
            'text',
            'is_archive',
            'accountant',
            'accountant_first_name',
            'accountant_last_name',
            'accountant_image',
            'sms_task',
            'manager',
            'task_file',
            'is_repeated',
            'end_date',
            'url',
            'created_date')

    def create(self, validated_data):
        files_data = self.context.get('view').request.FILES

        print(files_data, '----------------------------')
        task = Task.objects.create(
            name=validated_data.get('name', ),
            accountant=validated_data.get('accountant'),
            client=validated_data.get('client'),
            company=validated_data.get('company'),
            status=validated_data.get('status'),
            title=validated_data.get('title'),
            text=validated_data.get('text'),
            end_date=validated_data.get('end_date'),


            manager=validated_data.get('manager'),

        )
        for file_data in files_data.values():
            File.objects.create(task=task, file=file_data)
        return task
