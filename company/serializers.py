from .models import (
    Client,
    Company,
    TaxationSystem,
    TypeOfActivity
)
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from rest_framework.response import Response


class TypeOfActivitySerializer(serializers.HyperlinkedModelSerializer):
    # get_sr_price = serializers.SerializerMethodField('get_sr_price_func')

    class Meta:
        model = TypeOfActivity
        fields = (
            'id', 'name', 'url'
        )


class TaxationSystemSerializer(serializers.HyperlinkedModelSerializer):
    # get_sr_price = serializers.SerializerMethodField('get_sr_price_func')

    class Meta:
        model = TaxationSystem
        fields = (
            'id', 'name', 'url'
        )


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # get_sr_price = serializers.SerializerMethodField('get_sr_price_func')

    def get_sr_price_func(self, obj):
        return self.context['request'].user  # access the request object

    class Meta:
        model = Company
        fields = (
            'id', 'name', 'logo', 'client',
            'subscribe', 'accountant', 'HVHH',
            'address', 'created_date',
            'created_number', 'director_full_name',
            'packages', 'is_deleted', 'is_deleted_by_manager',
            'category', 'count_employees', 'type_of_activity', 'taxation_system', 'url'
        )
