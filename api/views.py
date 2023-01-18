from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Record,Sector,Country

from .serializers import RecordSerializer,SectorSerializer,CountrySerializer

class Records():
    list = Record.objects.all()
    serlize = RecordSerializer

class Sectors():
    list = Sector.objects.all()
    serlize = SectorSerializer

class Countries():
    list = Country.objects.all()
    serlize = CountrySerializer