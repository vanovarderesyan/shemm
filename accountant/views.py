from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework_guardian import filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
# from .serializers import VenderSerializer

from django.conf import settings

from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from django_filters import  rest_framework as filters
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework_jwt.settings import api_settings
from django.http import JsonResponse
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
from django.contrib.auth.hashers import make_password
from rest_framework_jwt.compat import get_username_field, PasswordField
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import exceptions
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    AccountantSerializer,
    UserSerializer,
    NoteSerializer
)
from .models import (
    Accountant,
    Note
)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def me(request, format=None):
    auth = get_authorization_header(request).split()
    payload = jwt_decode_handler(auth[1])
    user = Accountant.objects.get(user_id=payload['user_id']).get_fieldss()
    return JsonResponse(user)

@api_view(['POST'])
def login(request):
    username = request.data.get('username', None)
    password = request.data.get('password', None)
    if not username or not password:
        raise exceptions.AuthenticationFailed(('No credentials provided.'))

    credentials = {
        get_user_model().USERNAME_FIELD: username,
        'password': password
    }

    user = authenticate(**credentials)
    if user is None:
        raise exceptions.AuthenticationFailed(('Invalid username/password.'))

    if not user.is_active:
        raise exceptions.AuthenticationFailed(('User inactive or deleted.'))

    try:
        client = Accountant.objects.get(user=user)
    except:
        raise exceptions.AuthenticationFailed(('Invalid username/password.'))

    payload = jwt_payload_handler(user)

    return JsonResponse({
        'token': jwt_encode_handler(payload)
    })

class AccountantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer

    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        user.delete()

class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['accountant']