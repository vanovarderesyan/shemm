from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django_filters import Filter
from django_filters.fields import Lookup
import  django_filters
from .models import (
    Task,
    SMS,
    File,
    Company,
    Accountant,
    Repeated
)
from .serializers import (
    TaskSerializer,
    SMSSerializer,
    FileSerializer,
    RepeatedSerializer
)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request, '------------');
        return request.method in ["GET", "POST", "PUT"]


# Create your views here.

class TaskFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(field_name='created_date', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='created_date', lookup_expr='lte')
    company = django_filters.BaseInFilter(field_name="company")
    accountant = django_filters.ModelMultipleChoiceFilter(field_name="accountant", lookup_expr='gt',queryset=Accountant.objects.all())

    # company = django_filters.BaseInFilter(field_name="company", lookup_expr='in')

    class Meta:
        model = Task
        fields = ['accountant', 'manager', 'status', 'start_date', 'end_date', 'is_archive', 'company','client']




class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)
    # permission_classes = [IsAuthenticated | ReadOnly]

    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend]

    filterset_class = TaskFilter


class RepeatedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)
    # permission_classes = [IsAuthenticated | ReadOnly]

    queryset = Repeated.objects.all().order_by('-id')
    serializer_class = RepeatedSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['manager']


class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)
    permission_classes = [IsAuthenticated | ReadOnly]

    queryset = File.objects.all()
    serializer_class = FileSerializer


class SMSViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly,)
    permission_classes = [IsAuthenticated | ReadOnly]

    queryset = SMS.objects.all()
    serializer_class = SMSSerializer


@api_view(['POST'])
def setArchive(request):
    status = request.data.get('status', None)
    id = request.data.get('id', None)

    try:
        Task.objects.filter(id=id).update(is_archive=status)
    except:
        return JsonResponse({
            'status': "false"
        })
    return JsonResponse({
        'status': "ok"
    })
