from django.db import models

# Create your models here.
from client.models import Client
from  company.models import Company
from accountant.models import Accountant
from manager.models import Manager
from django.utils import timezone
from simple_history.models import HistoricalRecords

class Repeated(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, related_name='company_repeated',null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, related_name='client_repeated',null=True)
    name = models.CharField(max_length=255, blank=True)
    title = models.TextField(blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(blank=True,default=False)
    accountant = models.ForeignKey(Accountant, on_delete=models.CASCADE, related_name="accountant_repeated", null=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="manager_repeated", null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    repeated_type = models.IntegerField(blank=True,null=True)
    duration = models.PositiveIntegerField(blank=True,null=True)
    repeated_value = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, related_name='company_task',null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, related_name='client_task',null=True)
    repeated =  models.ForeignKey(Repeated, on_delete=models.SET_NULL, blank=True, related_name='task_repeated',null=True)
    is_repeated = models.BooleanField(blank=True,default=False)
    name = models.CharField(max_length=255, blank=True)
    title = models.TextField(blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    status = models.CharField(blank=True, default="new", max_length=60)
    is_archive = models.BooleanField(blank=True,default=False)
    accountant = models.ForeignKey(Accountant, on_delete=models.CASCADE, related_name="accountant_many", null=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="manager_many", null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name



class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=True, null=True)
    task = models.ForeignKey(Task, blank=True, related_name='task_file',on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.task.name


class SMS(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, blank=True, related_name='sms_task',on_delete=models.CASCADE, null=True, default=None)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    accountant = models.ForeignKey(Accountant, on_delete=models.CASCADE, related_name="sms_accountant", null=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="sms_manager", null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sms_client", null=True)

    def __str__(self):
        return self.text



