from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from .models import (Company, TaxationSystem, TypeOfActivity)
from .serializers import (CompanySerializer, TaxationSystemSerializer, TypeOfActivitySerializer)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse

from task.models import Task,Repeated

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in "GET"


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)

    queryset = Company.objects.all().filter(is_deleted_by_manager=False)
    serializer_class = CompanySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['accountant', 'packages','is_deleted']


class TypeOfActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)

    queryset = TypeOfActivity.objects.all()
    serializer_class = TypeOfActivitySerializer


class TaxationSystemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)

    queryset = TaxationSystem.objects.all()
    serializer_class = TaxationSystemSerializer


@api_view(['POST'])
def setDelted(request):
    id = request.data.get('id', None)

    try:

        company = Company.objects.get(pk=id)


        task = Task.objects.filter(company = company).count()
        rep_task = Repeated.objects.filter(company = company).count()

        print('--------**********------')
        print(task,rep_task,'*****************')

        if task or rep_task:
            return JsonResponse({
                'status': "false"
            })
        print(task,rep_task)


        Company.objects.filter(id=id).update(is_deleted=True)
    except:
        return JsonResponse({
            'status': "false"
        })
    return JsonResponse({
        'status': "ok"
    })

@api_view(['POST'])
def setDeltedManager(request):
    id = request.data.get('id', None)

    try:

        company = Company.objects.get(pk=id)


        task = Task.objects.filter(company = company).count()
        rep_task = Repeated.objects.filter(company = company).count()

        print('--------**********------')
        print(task,rep_task,'*****************')

        if task or rep_task:
            return JsonResponse({
                'status': "false"
            })
        print(task,rep_task)


        Company.objects.filter(id=id).update(is_deleted_by_manager=True)
    except:
        return JsonResponse({
            'status': "false"
        })
    return JsonResponse({
        'status': "ok"
    })
