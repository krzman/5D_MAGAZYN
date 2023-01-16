from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Workers(models.Model):
    name = models.CharField(max_length=32, verbose_name='Imię')
    surname = models.CharField(max_length=32, verbose_name='Nazwisko')
    phone = models.IntegerField(verbose_name='Nr telefonu', blank=True, null=True)
    company = models.CharField(max_length=32, verbose_name='Firma')


class Construction(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa')
    city = models.CharField(max_length=64, verbose_name='Miasto')
    contact = models.CharField(max_length=64, verbose_name='Kontakt')


class Tools(models.Model):
    nr = models.FloatField(max_length=16, verbose_name='Nr ewidencyjny')
    type = models.CharField(max_length=128, verbose_name='Typ')
    producer = models.CharField(max_length=64, verbose_name='Marka')
    capacity = models.CharField(max_length=32, verbose_name='Pojemność', blank=True)
    size = models.CharField(max_length=32, verbose_name='Wielkość', blank=True)
    date = models.DateField(verbose_name='Data pobrania', blank=True)
    workers = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='Pracownik', blank=True)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='Obiekt', blank=True)


class History(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Data')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Użytkownik')
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE, verbose_name='Narzędzie')
    workers = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='Pracownik')
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='Obiekt')
