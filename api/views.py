# Create your views here.
from rest_framework import generics
from scrap.models import Record,Sector,Country

from api.serializers import RecordSerializer,SectorSerializer,CountrySerializer

class Records(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class Sectors(generics.ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class Countries(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer