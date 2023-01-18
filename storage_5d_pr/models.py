import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Workers(models.Model):
    name = models.CharField(max_length=32, verbose_name='Imię')
    surname = models.CharField(max_length=32, verbose_name='Nazwisko')
    phone = models.IntegerField(verbose_name='Nr telefonu', blank=True, null=True)
    company = models.CharField(max_length=32, verbose_name='Firma')
    active = models.BooleanField(default=True, verbose_name='Aktywny')

    # Sortowanie według nazwiska
    class Meta:
        ordering = ['surname']

    def __str__(self):
        return (self.surname + ' ' + self.name)


class Construction(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa')
    city = models.CharField(max_length=64, verbose_name='Miasto')
    contact = models.CharField(max_length=64, verbose_name='Kontakt')

    # deleted = models.BooleanField(default=False, verbose_name='Usuń')

    def __str__(self):
        return (self.name + ' ' + self.city)


class Tools(models.Model):
    nr = models.FloatField(max_length=16, verbose_name='Nr ewidencyjny', unique=True)
    type = models.CharField(max_length=128, verbose_name='Typ')
    producer = models.CharField(max_length=64, verbose_name='Marka')
    capacity = models.CharField(max_length=32, verbose_name='Pojemność', blank=True)
    size = models.CharField(max_length=32, verbose_name='Wielkość', blank=True)
    date = models.DateField(verbose_name='Data pobrania', blank=True, default=datetime.date.today)
    workers = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='Pracownik', blank=True, null=True)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='Obiekt', blank=True,
                                     null=True)

    class Meta:
        ordering = ['nr']


class History(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data_wpisu')
    user = models.CharField(max_length=64, verbose_name='Użytkownik')
    tool_nr = models.FloatField(max_length=32, verbose_name='Nr ew', default=0.0, null=True)
    tool_type = models.CharField(max_length=128, verbose_name='Typ', default=0, null=True)
    tool_producer = models.CharField(max_length=64, verbose_name='Marka', default=0, null=True)
    tool_date = models.DateField(verbose_name='Data', blank=True, null=True)
    workers = models.CharField(max_length=64, verbose_name='Pracownik', blank=True, null=True)
    construction = models.CharField(max_length=64, verbose_name='Obiekt', blank=True, null=True)
    comment = models.TextField(max_length=164, verbose_name='Komentarz', blank=True)

    class Meta:
        ordering = ['-creation_date']
