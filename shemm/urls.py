"""shemm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_simplejwt import views as jwt_views

from accountant import views as accountant_views
from accountant.models import (Accountant, Note)
from client import views
from client.models import Client
from company.models import (Company, TaxationSystem, TypeOfActivity)
from company.views import (CompanyViewSet, TypeOfActivityViewSet, TaxationSystemViewSet, setDelted, setDeltedManager)
from manager import views as manager_views
from manager.models import Manager
from task.models import Task
from task.views import (
    TaskViewSet,
    SMSViewSet,
    FileViewSet,
    setArchive,
    RepeatedViewSet
    )
from utils import views as utils_views
from utils.models import (
    Subscribe,
    Advantages,
    CardService,
    Main,
    News,
    Packages,
    Service,
    Course,
    Info,
    Staff,
    Social
)
# rest api url

router = routers.DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'client-task', TaskViewSet)
router.register(r'repeated-task', RepeatedViewSet)

router.register(r'client-task-sms', SMSViewSet)
router.register(r'client-task-file', FileViewSet)

router.register(r'client-company', CompanyViewSet)
router.register(r'manager', manager_views.ManagerViewSet)
router.register(r'manager-company', manager_views.ManagerCompanyViewSet)

router.register(r'accountant', accountant_views.AccountantViewSet)
router.register(r'accountant-note', accountant_views.NodeViewSet)

router.register(r'course', utils_views.CourseViewSet)
router.register(r'social', utils_views.SocialViewSet)
router.register(r'advantages', utils_views.AdvantagesViewSet)
router.register(r'card-service', utils_views.CardServiceViewSet)
router.register(r'main', utils_views.MainViewSet)
router.register(r'news', utils_views.NewsViewSet)
router.register(r'packages', utils_views.PackagesViewSet)
router.register(r'service', utils_views.ServiceViewSet)
router.register(r'subscribe', utils_views.SubscribeViewSet)
router.register(r'info', utils_views.InfoViewSet)
router.register(r'staff', utils_views.StaffViewSet)
router.register(r'type-of-activity', TypeOfActivityViewSet)
router.register(r'taxation-system', TaxationSystemViewSet)

# admin url
admin.site.register(Client)
admin.site.register(Accountant)
admin.site.register(Manager)
admin.site.register(Subscribe)
admin.site.register(Advantages)
admin.site.register(CardService)
admin.site.register(Main)
admin.site.register(News)
admin.site.register(Packages)
admin.site.register(Service)
admin.site.register(Course)
admin.site.register(Company)
admin.site.register(Task)
admin.site.register(Info)
admin.site.register(Staff)
admin.site.register(Social)
admin.site.register(TaxationSystem)
admin.site.register(TypeOfActivity)

urlpatterns = [
                  path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
                  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

                  path('admin/', admin.site.urls),
                  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('api-token-auth/', obtain_jwt_token),
                  path('api/login/client', views.login),
                  path('api/client/me', views.me, name='get_me'),
                  path('api/login/manager', manager_views.login),
                  path('api/manager/me', manager_views.me),
                  path('api/manager/set/archive', setArchive),

                  path('api/manager/set/deleted/company', setDeltedManager),
                  path('api/deleted/company', setDelted),
                  path('api/login/accountant', accountant_views.login),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('api/accountant/me', accountant_views.me),
                  path('api-token-refresh/', refresh_jwt_token),
                  path('api-token-verify/', verify_jwt_token),
                  path('api/', include(router.urls)),
                  path('api/send-email/client/', views.send_email),
                  path('api/send-email/suggestion/', views.send_email_suggestion)

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
