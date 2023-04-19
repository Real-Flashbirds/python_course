from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User, Group

from .models import GDP, FieldGDP, Country, Region
from .serializers import (UserSerializer, GroupSerializer, GDPSerializer, CountrySerializer,
                          RegionSerializer,FieldGDPSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class GDPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = GDP.objects.all()
    serializer_class = GDPSerializer
    permission_classes = [permissions.IsAuthenticated]

class FieldGDPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows branches to be viewed or edited.
    """
    queryset = FieldGDP.objects.all()
    serializer_class = FieldGDPSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]