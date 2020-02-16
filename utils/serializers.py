from .models import (
    Course,
    Service,
    Packages,
    News,
    Main,
    CardService,
    Advantages,
    Subscribe,
    Info,
    Staff,
    Social

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


# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Course
#         fields = ('id','heading','description','text','image')

class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'heading', 'text', 'description', 'image')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'heading', 'description', 'text', 'image', 'to')


class CardServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardService
        fields = ('id', 'title')


class PackagesSerializer(serializers.HyperlinkedModelSerializer):
    service = CardServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Packages
        fields = ('id', 'name', 'price', 'service','url')


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'heading', 'description', 'text', 'image')


class MainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'heading', 'description', 'text', 'image')


class AdvantagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'


class SubscribeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'name', 'last_name', 'profession', 'image')

class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = ('id',  'link', 'image')

