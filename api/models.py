from django.db import models

# Create your models here.


class Sector(models.Model):
    name = models.CharField(max_length=140)

class Country(models.Model):
    name = models.CharField(max_length=140)

class Record(models.Model):
    signature_date = models.DateField()
    title = models.CharField(max_length=140)
    sectors = models.ManyToManyField(to=Sector)
    country = models.ForeignKey(to=Country,on_delete=models.CASCADE)
    signed_amount = models.CharField()