from django.contrib.auth.models import User, Group
from rest_framework import serializers

from Bank_project.banks.models import (Bank, Branch, Client, Account, )


class BankSerializer(serializers.ModelSerializer):
    class Meta:   # class Meta includes all meta information of the serializer
        model = Bank  # Original django model of Bank, as coded in banks/models.py.
        fields = '__all__'  # include all fields of Bank in the api.


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group