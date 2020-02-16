# Create your models here.
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

from django.utils import timezone

from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name='client_user')
    image = models.ImageField(blank=True, null=True)
    cover = models.ImageField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
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

    def __str__(self):
        return  self.user.last_name

    def get_fieldss(self):
        return dict({
            'id': self.id,
            'address': self.address,
            'phone': self.phone,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "password": self.user.password,
            "email": self.user.email,
            "image": str(self.image),
            "cover": str(self.cover)
        })

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# class Organisation(models.Model):
#     id = models.AutoField(primary_key=True)
#     logo = models.ImageField(blank=True, null=True)
#     name  = models.CharField(blank=True,null=True,max_length=255)
#     client = models.ForeignKey(Client,blank=True,related_name='client_organization',on_delete='cascade',default=None)
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
