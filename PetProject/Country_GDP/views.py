import os
from random import randrange

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
import json
from pyecharts.charts import Bar
from pyecharts import options as opts

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User, Group
from rest_framework.views import APIView

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

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return self.json_response(json.loads(self.bar_base()))

    def bar_base(self) -> Bar:
        c = (
            Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
            .dump_options_with_quotes()
        )
        return c

    # Create your views here.
    def response_as_json(self, data):
        json_str = json.dumps(data)
        response = HttpResponse(
            json_str,
            content_type="application/json",
        )
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def json_response(self, data, code=200):
        data = {
            "code": code,
            "msg": "success",
            "data": data,
        }
        return self.response_as_json(data)

    JsonResponse = json_response

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html").read())
