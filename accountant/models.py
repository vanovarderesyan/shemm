from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import os
import requests
from django.utils import timezone


class Accountant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name='accountant_user')
    image = models.ImageField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=25)
    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True)

    # def url(self):
    #     # returns a URL for either internal stored or external image url
    #     if self.externalURL:
    #         return self.externalURL
    #     else:
    #         # is this the best way to do this??
    #         return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.image)))
    def get_fieldss(self):
        return dict({
            'id': self.id,
            'phone': self.phone
        })

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return  self.user.last_name


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    accountant = models.ForeignKey(Accountant, on_delete=models.CASCADE, blank=True, related_name='accountant_note')
    title = models.TextField(blank=True, null=True)
    end_date = models.DateField(null=True, blank=True)
