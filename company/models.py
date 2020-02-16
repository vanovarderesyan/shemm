from django.db import models

# Create your models here.
from client.models import Client
from accountant.models import Accountant
from utils.models import Subscribe
from django.utils import timezone
from utils.models import Packages


class TypeOfActivity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class TaxationSystem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, blank=True, related_name='client_company', on_delete='cascade', default=None)
    logo = models.ImageField(blank=True, null=True)
    subscribe = models.ForeignKey(Subscribe, on_delete=models.CASCADE, blank=True, related_name='subscribe', null=True)
    name = models.CharField(max_length=255, blank=True)
    HVHH = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    accountant = models.ManyToManyField(Accountant, related_name="accountant_many_company", null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    created_number = models.IntegerField(null=True, blank=True)
    director_full_name = models.TextField(null=True, blank=True)
    category = models.IntegerField(null=True, blank=True)
    count_employees = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False,blank=True)
    is_deleted_by_manager = models.BooleanField(default=False,blank=True)
    type_of_activity = models.ManyToManyField(TypeOfActivity, null=True, blank=True)
    packages = models.ForeignKey(Packages, null=True, blank=True, on_delete=models.DO_NOTHING,
                                 related_name="packages_company")
    taxation_system = models.ForeignKey(TaxationSystem, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
