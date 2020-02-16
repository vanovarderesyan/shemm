from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.name)


class Main(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=255, blank=True)
    text = RichTextField('Text')
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(blank=True)

    def __str__(self):
        return str(self.description)

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=255, blank=True)
    text = RichTextField('Text')
    description = models.CharField(max_length=255, blank=True)
    to = models.CharField(max_length=255, blank=True)
    image = models.FileField(max_length=255, blank=True)

    def __str__(self):
        return str(self.heading)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=255, blank=True)
    text = RichTextField('text')
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(max_length=255, blank=True)

    def __str__(self):
        return str(self.description)

class Advantages(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return str(self.title)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    text = RichTextField('Text')
    image = models.FileField(max_length=255, blank=True)

    def __str__(self):
        return str(self.description)


class CardService(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.id)


class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True)
    service = models.ManyToManyField(CardService, related_name="service_many", verbose_name='service_many')

    def __str__(self):
        return '%d: %s' % (self.price, self.name)


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255, blank=True)
    text = RichTextField('Text')
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.name)


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    profession = models.CharField(max_length=255, blank=True)
    image = models.FileField(max_length=255, blank=True)

    def __str__(self):
        return str(self.name)


class Social(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.TextField(max_length=255, blank=True)
    image = models.FileField(max_length=255, blank=True)

    def __str__(self):
        return str(self.link)
