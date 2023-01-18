from rest_framework import serializers
from .models import Record,Sector,Country

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = '__all__'
