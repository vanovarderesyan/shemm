from rest_framework import viewsets
from rest_framework.authentication import (
    get_authorization_header
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission
from rest_framework import permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework_jwt.settings import api_settings
from django.http import JsonResponse
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
from django.contrib.auth import authenticate, get_user_model

# Create your views here.
from rest_framework import exceptions

from .serializers import (
    ClientSerializer
)
from .models import (
    Client
)

from django.core.mail import send_mail


def sendEmailTo(email):

    return send_mail(
        'ROPA registered',
        'Hello, Welcome to the ROPA project',
        'notify@ropa.nyc',
        [email],
        fail_silently=False,
    )


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def me(request, format=None):
    auth = get_authorization_header(request).split()
    payload = jwt_decode_handler(auth[1])
    user = Client.objects.get(user_id=payload['user_id']).get_fieldss()
    return JsonResponse(user)


@api_view(['POST'])
def send_email(request, format=None):
    send_mail(
        request.data.get('name'),
        request.data.get('request'),
        'vano.varderesyan94@gmail.com',
        [request.data.get('email')],
        fail_silently=False,
    )

    return JsonResponse({"message":"ok"})

@api_view(['POST'])
def send_email_suggestion(request, format=None):
    send_mail(
        'առաջարկություՆ',
        'ծառայության անուն    :    ' + request.data.get('suggestion')+ '\n' + 'email    :   '+str(request.data.get('email')) + '\n' + 'name    :   '+str(request.data.get('name')) + '\n' + 'phone    :   '+str(request.data.get('phone')),

        'vano.varderesyan94@gmail.com',
        ['vano.varderesyan94@gmail.com'],
        fail_silently=False,
    )

    return JsonResponse({"message":"ok"})

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
        client = Client.objects.get(user=user)
    except:
        raise exceptions.AuthenticationFailed(('Invalid username/password.'))

    payload = jwt_payload_handler(user)

    return JsonResponse({
        'token': jwt_encode_handler(payload)
    })


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ["GET","POST"]

class UpdatePermision(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user,'*********')
        if request.method in permissions.SAFE_METHODS:
            return  True
        return obj.user == request.user



class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    print(Client.objects,'-----------')

    # permission_classes = [UpdatePermision ]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        user.delete()

# class OrganisationViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     print(Client.objects, '-----------')
#     # permission_classes = (ReadOnly,)
#
#     queryset = Organisation.objects.all()
#     serializer_class = OrganisationSerializer

