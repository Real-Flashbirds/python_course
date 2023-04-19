from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import GDP, Country, Region, FieldGDP


class GDPSerializer(serializers.ModelSerializer):
    class Meta:   # class Meta includes all meta information of the serializer
        model = GDP  # Original django model of Bank, as coded in banks/models.py.
        fields = '__all__'  # include all fields of Bank in the api.


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class FieldGDPSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FieldGDP


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group