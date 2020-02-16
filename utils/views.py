from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated

from .models import (
    Course,
    Subscribe,
    Advantages,
    CardService,
    Main,
    News,
    Packages,
    Service,
    Info,
    Staff,
    Social
)
from .serializers import (
    CourseSerializer,
    AdvantagesSerializer,
    CardServiceSerializer,
    MainSerializer,
    NewsSerializer,
    PackagesSerializer,
    ServiceSerializer,
    SubscribeSerializer,
    InfoSerializer,
    StaffSerializer,
    SocialSerializer
)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in "GET"

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AdvantagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

class SubscribeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class CardServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = CardService.objects.all()
    serializer_class = CardServiceSerializer

class MainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Main.objects.all()
    serializer_class = MainSerializer

class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = News.objects.all()
    serializer_class = NewsSerializer

class PackagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class StaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (ReadOnly)
    # permission_classes = (,)


    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class SocialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly,)

    queryset = Social.objects.all()
    serializer_class = SocialSerializer


