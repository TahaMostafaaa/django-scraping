# Create your views here.
from rest_framework import generics
from scrap.models import Record,Sector,Country

from .serializers import RecordSerializer,SectorSerializer,CountrySerializer

class Records(generics.ListAPIView):
    list = Record.objects.all()
    serlize = RecordSerializer

class Sectors(generics.ListAPIView):
    list = Sector.objects.all()
    serlize = SectorSerializer

class Countries(generics.ListAPIView):
    list = Country.objects.all()
    serlize = CountrySerializer